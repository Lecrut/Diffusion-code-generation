import operator

def group_by_attribute(objects, attr):
    if not objects or not hasattr(objects[0], attr):
        raise ValueError("Invalid input: objects must be non-empty and have the specified attribute")
    
    grouped = {}
    for obj in objects:
        attr_value = getattr(obj, attr)
        if attr_value not in grouped:
            grouped[attr_value] = []
        grouped[attr_value].append(obj)
    return grouped

if __name__ == '__main__':
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 30)]
    grouped_by_age = group_by_attribute(people, 'age')
    print(grouped_by_age)