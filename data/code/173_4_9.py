import operator

def group_by_attribute(objects, attr):
    if not objects or not attr:
        return {}
    
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
    for age, people_list in grouped_by_age.items():
        print(f"Age {age}: {[person.name for person in people_list]}")