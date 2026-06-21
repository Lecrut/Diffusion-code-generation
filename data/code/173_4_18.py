import operator

def group_by_attribute(objects, attr):
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
    
    for age_group in sorted(grouped_by_age.keys()):
        print(f"Age {age_group}:")
        for person in grouped_by_age[age_group]:
            print(f"  Name: {person.name}, Age: {person.age}")