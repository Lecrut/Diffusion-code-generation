class CustomObject:
    def __init__(self, value):
        self.value = value

def custom_sort_key(obj):
    return obj.value

def sort_custom_objects(objects):
    return sorted(objects, key=custom_sort_key)

if __name__ == '__main__':
    objects = [CustomObject(3), CustomObject(1), CustomObject(2)]
    sorted_objects = sort_custom_objects(objects)
    print([obj.value for obj in sorted_objects])