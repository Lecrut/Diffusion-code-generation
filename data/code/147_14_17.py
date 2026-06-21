from operator import attrgetter

class CustomObject:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

def sort_custom_objects(objects: list[CustomObject], attribute: str) -> list[CustomObject]:
    if not isinstance(objects, list) or not all(isinstance(obj, CustomObject) for obj in objects):
        raise ValueError("First argument must be a list of CustomObject instances")
    
    if not isinstance(attribute, str) or not hasattr(CustomObject, attribute):
        raise ValueError(f"Second argument must be a valid attribute name of CustomObject: {attribute}")
    
    return sorted(objects, key=attrgetter(attribute))

if __name__ == '__main__':
    objects = [
        CustomObject('apple', 3),
        CustomObject('banana', 1),
        CustomObject('cherry', 2)
    ]
    try:
        sorted_objects = sort_custom_objects(objects, 'value')
        for obj in sorted_objects:
            print(f'{obj.name}: {obj.value}')
    except ValueError as e:
        print(e)