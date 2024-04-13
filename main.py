class Student:
    def __init__(self, name="none"):
        self.name = name

    def __str__(self):
        return f"Hello, my name is {self.name}"

    def __del__(self):
        print("I'm graduated))))")

stud = Student("Andriy")
print(stud)


# class Student:
#     amount_of_students = 0
#     def __init__(self, height=0, name="noname", mark=0):
#         self.name = name
#         self.mark = mark
#         self.height = height
#         print("Зріст ",self.name,": ", self.height)
#         Student.amount_of_students += 1
#
#     def growUp(self):
#         self.height += 10
#
#     def markUp(self, mark=0):
#         self.mark += mark
#
# stepan = Student()
# maxym = Student(height=180, name="Максим", mark=8)
# kate = Student(height=170, name="Катя")
#
# print(maxym.mark)
# maxym.markUp(2)
# print(maxym.mark)


# print("Зріст Макса: ", maxym.height)
# print("Зріст Каті: ", kate.height)
# print("Зріст Степана: ", stepan.height)

