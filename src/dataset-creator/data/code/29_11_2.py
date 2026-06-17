import sys
class Student:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
class RecordManager:
    def __init__(self):
        self._records = []
    def add_student(self, student_name):
        new_record = Student(student_name)
        self._records.append(new_record)
    def get_all_names(self):
        names = [record.name for record in self._records]
        return '\n'.join(names)
if __name__ == '__main__':
    manager = RecordManager()
    manager.add_student("Alice Johnson")
    manager.add_student("Bob Smith")
    manager.add_student("Charlie Brown")
    print(manager.get_all_names())