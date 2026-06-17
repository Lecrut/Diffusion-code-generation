from dataclasses import dataclass
@dataclass
class Student:
    name: str
def main():
    students = [Student("Alice"), Student("Bob")]
    serialized_data = [[s.name] for s in students]
    print(serialized_data)
if __name__ == '__main__':
    main()