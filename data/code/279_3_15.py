class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name}: {self.age}")

if __name__ == '__main__':
    sample_people = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35
    }

    people_instances = [Person(name, age) for name, age in sample_people.items()]

    for person in people_instances:
        person.display_info()