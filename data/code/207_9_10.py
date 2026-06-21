import operator

class CustomObject:
    def __init__(self, value):
        self.value = value

def find_max_in_custom_objects(objects, attribute='value'):
    if not objects:
        raise ValueError("Input list cannot be empty")
    
    attr_getter = operator.attrgetter(attribute)
    max_object = max(objects, key=attr_getter)
    return max_object.value

if __name__ == '__main__':
    sample_objects = [CustomObject(3), CustomObject(1), CustomObject(4)]
    max_value = find_max_in_custom_objects(sample_objects)
    print(max_value)