import operator

class CustomObject:
    def __init__(self, value):
        self.value = value

def sort_custom_objects(objects, attribute_name):
    return sorted(objects, key=operator.attrgetter(attribute_name))

if __name__ == '__main__':
    objects = [CustomObject(3), CustomObject(1), CustomObject(2)]
    sorted_objects = sort_custom_objects(objects, 'value')
    print([obj.value for obj in sorted_objects])