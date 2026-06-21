class CustomObject:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

def sort_custom_objects(objects):
    objects.sort(key=lambda obj: obj.get_value())
    return objects

if __name__ == '__main__':
    objects = [CustomObject(5), CustomObject(2), CustomObject(8), CustomObject(1), CustomObject(9), CustomObject(3)]
    sorted_objects = sort_custom_objects(objects)
    for obj in sorted_objects:
        print(obj.get_value())