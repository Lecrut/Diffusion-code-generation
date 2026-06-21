class CustomObject:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"CustomObject({self.value})"

def sort_custom_objects(objects):
    objects.sort(key=lambda obj: obj.value)
    return objects

if __name__ == '__main__':
    objects = [CustomObject(5), CustomObject(2), CustomObject(8), CustomObject(1), CustomObject(9), CustomObject(3)]
    print("Original list:", objects)
    sorted_objects = sort_custom_objects(objects)
    print("Sorted list:", sorted_objects)