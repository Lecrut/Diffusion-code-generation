import operator

def group_by_attribute(objects, attr):
    return {attr_value: [] for obj in objects for attr_value in (getattr(obj, attr),)}

if __name__ == '__main__':
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 30)]
    
    grouped_by_age = group_by_attribute(people, 'age')
    print(grouped_by_age)