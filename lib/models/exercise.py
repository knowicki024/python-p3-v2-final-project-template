import sqlite3 #database

CONN = sqlite3.connect("lib/gym.db") #connection
CURSOR = CONN.cursor() #pointer for the connection, row by row

class Exercise:

    # constructor
    def __init__(self, name, id=None):
        self.id = id # unknown now
        self.name = name # Need to make a property

    def display_info(self):
        print(f"Exercise Name: {self.name}")

    @classmethod #affects the whole table, not just one row
    def create_table(cls): #this class as a parameter
        query = """
            CREATE TABLE IF NOT EXISTS exercise (
            id INTEGER PRIMARY KEY,
            name TEXT);
        """
        CURSOR.execute(query) #CURSOR takes the 'query' and executes it
        CONN.commit() #save the changes
    
    @classmethod
    def drop_table(cls):
        query = """
            DROP TABLE exercise;
        """
        CURSOR.execute(query)
        CONN.commit()

    #instance method / not class method
    def save(self):
        query = """
            INSERT INTO exercise (name)
            VALUES (?);
        """
        CURSOR.execute(query, (self.name,))
        CONN.commit() #save the changes
        self.id = CURSOR.lastrowid #update the id
        return self.id #return the id
    
    @classmethod
    def create(cls, name):
        exercise = Exercise(name)
        return exercise.save() #return the id
    
    @classmethod
    def new_form_db(cls, row):
        exercise = cls(
            name = row[1], #row at index 1 is the name
            id = row[0] #row at index 0 is the id
        )
        print(exercise.name, exercise.id)
        return exercise
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM exercise;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        exercises = []
        for row in rows:
            exercise = cls.new_form_db(row)
            exercises.append(exercise)
        return exercises




# Exercises
spin_class = Exercise("Spin Class")
boxing = Exercise("Boxing")
zumba = Exercise("Zumba")
step_class = Exercise("Step Class")
