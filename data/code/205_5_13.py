class CustomObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_value(self):
        return self.value

def sort_custom_objects(objects):
    return sorted(objects, key=lambda obj: obj.get_value())

if __name__ == '__main__':
    objects = [
        CustomObject("A", 3),
        CustomObject("B", 1),
        CustomObject("C", 2)
    ]
    sorted_objects = sort_custom_objects(objects)
    for obj in sorted_objects:
        print(f"{obj.name}: {obj.value}")