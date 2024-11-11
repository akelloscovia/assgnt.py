#OOP
# i)Add  a constructor for the class cohort
# ii)Create a method / fuction to the class that prints the cohort name and the total number of students 
#iii)Create a new instance of the cohort class.


#Solutions  
# Constructor for the class
class cohort:
    def __init__(self, name, start_date, end_date, total_students):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.total_students = total_students
     #ii)
cohortiv = cohort("PACOD I", "2024-09-01", "2025-08-31", 30)
print(" cohort name:",cohortiv.name)
print("cohort start date:",cohortiv.start_date)
print("cohort date:",cohortiv.end_date)
print("cohort student number:",cohortiv.total_students)
      #iii)
class cohort:
    def __init__(self, name, start_date, end_date, total_students):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.total_students = total_students
cohortv = cohort("PACOD II", "2024-09-01", "2025-08-31", 30)
print(" cohort name:",cohortv.name)
print("cohort start date:",cohortv.start_date)
print("cohort date:",cohortv.end_date)
print("cohort student number:",cohortv.total_students) 