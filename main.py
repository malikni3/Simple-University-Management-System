from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @abstractmethod
    def display_info(self):

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

class Student(Person):

    def __init__(self, name, age, email, student_id, major, gpa):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.major = major
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            print("Error: GPA must be between 0.0 and 4.0")

    def display_info(self):
        print("--- Student Information ---")
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"GPA: {self.__gpa}")
        print("-" * 25)

class Professor(Person):

    def __init__(self, name, age, email, department, salary):
        super().__init__(name, age, email)
        self.department = department
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Error: Salary must be a positive value.")

    def display_info(self):
        print("--- Professor Information ---")
        super().display_info()
        print(f"Department: {self.department}")
        print("-" * 25)

class University:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.professors = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' has been added to the university.")

    def add_professor(self, professor):
        self.professors.append(professor)
        print(f"Professor '{professor.name}' has been added to the university.")

    def show_all_people(self):
        print(f"\n===== Displaying All People at {self.name} =====")
        for student in self.students:
            student.display_info()
        for professor in self.professors:
            professor.display_info()

uni = University("University of Science and Technology")

student1 = Student("Ahmed Khaled", 20, "ahmed@example.com", "S12345", "Computer Science", 3.5)
student2 = Student("Fatima Ali", 22, "fatima@example.com", "S67890", "Electrical Engineering", 3.8)
uni.add_student(student1)
uni.add_student(student2)

prof1 = Professor("Mohammed Abdullah", 45, "mohammed@example.com", "Computer Science Dept", 70000)
prof2 = Professor("Sara Mahmoud", 50, "sara@example.com", "Engineering Dept", 85000)
uni.add_professor(prof1)
uni.add_professor(prof2)

uni.show_all_people()

print("\n--- Updating Ahmed's GPA ---")
print(f"Ahmed's current GPA: {student1.get_gpa()}")
student1.set_gpa(3.6)
print(f"Ahmed's new GPA: {student1.get_gpa()}")

print("\n--- Attempting to set an invalid GPA ---")
student1.set_gpa(5.0)

print("\n--- Displaying Ahmed's info after update ---")

student1.display_info()
