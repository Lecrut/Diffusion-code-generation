class CustomObject:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def sort_objects(data):
        return sorted(data, key=lambda obj: obj.value)

if __name__ == '__main__':
    objects = [CustomObject(5), CustomObject(2), CustomObject(8), CustomObject(1)]
    print("Original objects:", [obj.value for obj in objects])
    sorted_objects = CustomObject.sort_objects(objects)
    print("Sorted objects:", [obj.value for obj in sorted_objects])