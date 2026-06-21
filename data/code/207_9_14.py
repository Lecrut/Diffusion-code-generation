import operator

class CustomObject:
    def __init__(self, value):
        self.value = value

def find_max_by_attribute(objects, attribute_name):
    if not objects:
        raise ValueError("Input list cannot be empty")
    
    max_obj = max(objects, key=operator.attrgetter(attribute_name))
    return getattr(max_obj, attribute_name)

if __name__ == '__main__':
    sample_objects = [
        CustomObject(10),
        CustomObject(5),
        CustomObject(20)
    ]
    max_value = find_max_by_attribute(sample_objects, 'value')
    print(max_value)