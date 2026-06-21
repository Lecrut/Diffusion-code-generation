class CustomObject:
    def __init__(self, value):
        self.value = value

def sort_custom_objects(data):
    if not all(isinstance(item, CustomObject) for item in data):
        raise ValueError("All elements must be instances of CustomObject")
    
    return sorted(data, key=lambda obj: obj.value)

if __name__ == '__main__':
    objects = [CustomObject(5), CustomObject(2), CustomObject(8), CustomObject(1), CustomObject(9), CustomObject(3)]
    print("Original list:")
    for obj in objects:
        print(obj.value, end=' ')
    
    sorted_objects = sort_custom_objects(objects)
    print("\nSorted list:")
    for obj in sorted_objects:
        print(obj.value, end=' ')