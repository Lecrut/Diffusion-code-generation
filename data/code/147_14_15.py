from operator import attrgetter

class CustomObject:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

def sort_custom_objects(objects: list[CustomObject], attribute: str) -> list[CustomObject]:
    return sorted(objects, key=attrgetter(attribute))

if __name__ == '__main__':
    objects = [
        CustomObject('apple', 3),
        CustomObject('banana', 1),
        CustomObject('cherry', 2)
    ]
    
    sorted_by_name = sort_custom_objects(objects, 'name')
    for obj in sorted_by_name:
        print(f'{obj.name}: {obj.value}')
    
    sorted_by_value = sort_custom_objects(objects, 'value')
    for obj in sorted_by_value:
        print(f'{obj.name}: {obj.value}')