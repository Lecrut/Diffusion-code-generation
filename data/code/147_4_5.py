class CustomObject:
    def __init__(self, value):
        self.value = value

def sort_custom_objects(objects):
    return sorted(objects, key=lambda obj: obj.value)

if __name__ == '__main__':
    objects = [CustomObject(3), CustomObject(1), CustomObject(2)]
    sorted_objects = sort_custom_objects(objects)
    for obj in sorted_objects:
        print(obj.value)