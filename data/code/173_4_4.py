import operator

def group_by_attribute(objects, attr):
    grouped = {}
    for obj in objects:
        key = getattr(obj, attr)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(obj)
    return grouped

if __name__ == '__main__':
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 30)]
    grouped_by_age = group_by_attribute(people, 'age')
    print(grouped_by_age)