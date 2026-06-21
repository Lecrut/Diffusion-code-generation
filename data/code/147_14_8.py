from operator import attrgetter

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def sort_by_attribute(objects: list, attribute: str) -> list:
    return sorted(objects, key=attrgetter(attribute))

if __name__ == '__main__':
    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
    sorted_people = sort_by_attribute(people, 'age')
    for person in sorted_people:
        print(f"{person.name}: {person.age}")