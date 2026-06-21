class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def sort_people(people):
    return sorted(people, key=lambda person: person.age)

if __name__ == '__main__':
    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
    sorted_people = sort_people(people)
    for person in sorted_people:
        print(f"{person.name}: {person.age}")