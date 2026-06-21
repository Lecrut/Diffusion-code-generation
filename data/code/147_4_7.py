class CustomObject:
    def __init__(self, value):
        self.value = value

def sort_custom_objects(objects, key_attr):
    return sorted(objects, key=lambda obj: getattr(obj, key_attr))

if __name__ == '__main__':
    objects = [CustomObject(3), CustomObject(1), CustomObject(2)]
    sorted_objects = sort_custom_objects(objects, 'value')
    print([obj.value for obj in sorted_objects])