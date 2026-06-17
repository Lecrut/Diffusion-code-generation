from dataclasses import dataclass
@dataclass
class Student:
    name: str
def main():
    students = [Student(name="Alice"), Student(name="Bob")]
    for student in students:
        print(f"Name: {student.name}")
if __name__ == '__main__':
    main()