print("Hello World")

class Student:
    def __init__(self, name: str, age: int, email: str | None=None):
        self.name = name
        self.age = age

    def a(self):
        return 1 + 2

    def __str__(self):
        return f'{self.name.title()} {self.age} years old'