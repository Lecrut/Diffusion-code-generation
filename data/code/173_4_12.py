import operator

def group_by_attribute(objects, attr):
    return {attr_value: [] for obj in objects for attr_value in (getattr(obj, attr),)}

class GroupedObjects:
    def __init__(self, objects, attr):
        self.objects = objects
        self.attr = attr
        self.grouped = operator.itemgetter(attr)(objects)

    def get_grouped(self):
        return self.grouped

if __name__ == '__main__':
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 30)]
    grouped_obj = GroupedObjects(people, 'age')
    print(grouped_obj.get_grouped())