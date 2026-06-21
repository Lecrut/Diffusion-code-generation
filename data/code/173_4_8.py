import operator

def group_by_attribute(objects, attr):
    return {getattr(obj, attr): [] for obj in objects}

if __name__ == '__main__':
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 30)]
    
    grouped_people = group_by_attribute(people, 'age')
    print(grouped_people)