from operator import attrgetter

class CustomObject:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

def validate_attribute(obj: CustomObject, attribute: str) -> bool:
    return hasattr(obj, attribute)

def sort_custom_objects(objects: list[CustomObject], attribute: str) -> list[CustomObject]:
    if not all(validate_attribute(obj, attribute) for obj in objects):
        raise ValueError(f"Attribute '{attribute}' not found in all CustomObjects")
    
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