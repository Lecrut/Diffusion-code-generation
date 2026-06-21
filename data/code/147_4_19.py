MAX_VALUE = 100

class CustomObject:

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value * MAX_VALUE

def sort_custom_objects(objects):
    return sorted(objects, key=lambda obj: obj.get_value(), reverse=True)
if __name__ == '__main__':
    objects = [CustomObject(3), CustomObject(1), CustomObject(2)]
    sorted_objects = sort_custom_objects(objects)
    for obj in sorted_objects:
        print(obj.value * MAX_VALUE)