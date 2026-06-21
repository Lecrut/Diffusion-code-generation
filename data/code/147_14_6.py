from operator import attrgetter

class CustomObject:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    @staticmethod
    def sort_key(obj):
        return obj.value

def sort_custom_objects(objects: list[CustomObject]) -> list[CustomObject]:
    return sorted(objects, key=CustomObject.sort_key)

if __name__ == '__main__':
    objects = [
        CustomObject('apple', 3),
        CustomObject('banana', 1),
        CustomObject('cherry', 2)
    ]
    sorted_objects = sort_custom_objects(objects)
    for obj in sorted_objects:
        print(f'{obj.name}: {obj.value}')