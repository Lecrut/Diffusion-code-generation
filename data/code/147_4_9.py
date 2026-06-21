class CustomObject:
    def __init__(self, value):
        self.value = value

def sort_custom_objects(obj_list):
    if not all(isinstance(obj, CustomObject) for obj in obj_list):
        raise ValueError("All elements in the list must be instances of CustomObject.")
    return sorted(obj_list, key=lambda obj: obj.value)

if __name__ == '__main__':
    objects = [CustomObject(3), CustomObject(1), CustomObject(2)]
    try:
        sorted_objects = sort_custom_objects(objects)
        for obj in sorted_objects:
            print(obj.value)
    except ValueError as e:
        print(e)