class CustomObject:
    def __init__(self, value):
        self.value = value

def validate_input(data):
    if not all(isinstance(item, CustomObject) for item in data):
        raise ValueError("All elements must be instances of CustomObject")

def sort_custom_objects(obj_list):
    validate_input(obj_list)
    return sorted(obj_list, key=lambda obj: obj.value)

if __name__ == '__main__':
    objects = [CustomObject(3), CustomObject(1), CustomObject(2)]
    sorted_objects = sort_custom_objects(objects)
    for obj in sorted_objects:
        print(obj.value)