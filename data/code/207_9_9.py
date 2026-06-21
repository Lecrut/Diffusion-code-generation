import operator

class CustomObject:
    def __init__(self, value):
        self.value = value

def find_max_by_attribute(objects, attribute_name):
    return max(objects, key=operator.attrgetter(attribute_name))

if __name__ == '__main__':
    objects = [CustomObject(10), CustomObject(20), CustomObject(5)]
    max_object = find_max_by_attribute(objects, 'value')
    print(max_object.value)