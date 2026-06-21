import operator

class CustomObject:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

def sort_custom_objects(objects: list) -> list:
    return sorted(objects, key=operator.attrgetter('value'))

if __name__ == '__main__':
    objects = [CustomObject('a', 3), CustomObject('b', 1), CustomObject('c', 2)]
    sorted_objects = sort_custom_objects(objects)
    for obj in sorted_objects:
        print(f'{obj.name}: {obj.value}')