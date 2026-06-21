import operator
from collections import defaultdict

def group_by_attribute(objects, attr):
    return {attr_value: [] for obj in objects for attr_value in (getattr(obj, attr),)}

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 30)]
    grouped_people_by_age = group_by_attribute(people, 'age')
    for person in people:
        grouped_people_by_age[person.age].append(person.name)
    print(grouped_people_by_age)