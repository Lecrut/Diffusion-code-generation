class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name}: {self.age}")

if __name__ == '__main__':
    people = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35
    }

    person_objects = [Person(name, age) for name, age in people.items()]

    for person in person_objects:
        person.display_info()