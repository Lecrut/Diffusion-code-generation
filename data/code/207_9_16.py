import operator

class CustomObject:
    def __init__(self, value):
        self.value = value

def find_max_by_attribute(objects, attr_name):
    if not objects:
        raise ValueError("Input list cannot be empty")
    
    max_object = max(objects, key=operator.attrgetter(attr_name))
    return getattr(max_object, attr_name)

if __name__ == '__main__':
    obj1 = CustomObject(5)
    obj2 = CustomObject(3)
    obj3 = CustomObject(9)
    
    objects = [obj1, obj2, obj3]
    max_value = find_max_by_attribute(objects, 'value')
    print(max_value)