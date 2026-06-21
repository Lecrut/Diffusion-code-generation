import operator

class CustomObject:

    def __init__(self, value):
        self.value = value

def find_max_object(objects, attr_name):
    if not objects:
        raise ValueError('Input list cannot be empty')
    max_obj = max(objects, key=operator.attrgetter(attr_name))
    return max_obj.value
if __name__ == '__main__':
    obj1 = CustomObject(10)
    obj2 = CustomObject(20)
    obj3 = CustomObject(15)
    objects = [obj1, obj2, obj3]
    max_val = find_max_object(objects, 'value')
    print(max_val)