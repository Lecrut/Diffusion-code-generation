class CustomObject:
    def __init__(self, value):
        self.value = value

def sort_custom_objects(objects):
    objects.sort(key=lambda obj: obj.value)
    return objects

if __name__ == '__main__':
    sample_objects = [CustomObject(5), CustomObject(2), CustomObject(8), CustomObject(1), CustomObject(9), CustomObject(3)]
    sorted_objects = sort_custom_objects(sample_objects)
    print([obj.value for obj in sorted_objects])