import operator
from collections import defaultdict

def group_by_attribute(objects, attr):
    if not callable(attr):
        raise ValueError("The second argument must be a callable attribute.")
    
    grouped = defaultdict(list)
    for obj in objects:
        attr_value = attr(obj)
        grouped[attr_value].append(obj)
    return dict(grouped)

if __name__ == '__main__':
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 30)]
    grouped_by_age = group_by_attribute(people, lambda person: person.age)
    print(grouped_by_age)