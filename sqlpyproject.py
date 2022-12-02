import mysql.connector as mc


conn = mc.connect(host='localhost', user='root',
                  password='YU_oppdivide!20', database="menagerie")


c = conn.cursor()
db = "show databases"
# c.execute("CREATE TABLE pet(name varchar(20), owner VARCHAR(20), species VARCHAR(20),sex CHAR(8), birth DATE, death DATE)")

# c.execute("INSERT INTO pet (name,owner,species,sex,birth,death) VALUES \
#     ('Fluffy','Harold', 'cat', 'f','1993-02-04',NULL),\
#     ('Claws','Gwen', 'cat', 'm','1994-03-17',NULL),\
#     ('Buffy','Harold', 'dog', 'f','1989-05-13',NULL),\
#     ('Fang','Benny', 'dog', 'm','1990-08-27',NULL),\
#     ('Bowser','Diane', 'dog', 'm','1979-08-31','1995-07-29'),\
#     ('Chripy','Gwen', 'bird', 'f','1998-09-11',NULL),\
#     ('Whistler','Gwen', 'bird', 'NULL','1997-12-09',NULL),\
#     ('Slim','Benny', 'snake', 'm','1996-04-29',NULL),\
#     ('Puffball','Diane', 'hamster', 'f','1999-03-30',NULL)")
# conn.commit()

# c.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'")
# for pet in c:
#     print(pet)


# c.execute('SELECT * FROM pet')
# co =c.fetchall()
# for i in co:
#     print(i[0],i[1],i[2],i[3],i[4],i[5])

# def commit_close():
#
#     conn.commit()
#     c.close()
#     conn.close()

# for db in c:
#     print(f"{db[0]}"

# def drop():
#     c.execute("drop database if exists then menagerie")
#     for db in c:
#         print(f"db[0]")

# sql = "INSERT INTO pet (name, owner, species, sex, birth, death) VALUES($s,%s,%s,%s,%s,%s)"
#
# values=[
#     ('Fluffy')
# ]

#
# c.execute("SELECT name, birth FROM pet")
# for pet in c:
#     print(pet)

# c.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner")
# for pet in c:
#     print(pet)

c.execute("SELECT name, birth, MONTH(birth) FROM pet;")
co = c.fetchall()

for c in co:
    print(c)
