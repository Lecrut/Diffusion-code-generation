class CustomObject:
    def __init__(self, value):
        self.value = value

def sort_custom_objects(data):
    data.sort(key=lambda obj: obj.value)
    return data

if __name__ == '__main__':
    objects = [CustomObject(5), CustomObject(2), CustomObject(8), CustomObject(1), CustomObject(9), CustomObject(3)]
    sorted_objects = sort_custom_objects(objects)
    print("Sorted objects by value:", [(obj.value) for obj in sorted_objects])