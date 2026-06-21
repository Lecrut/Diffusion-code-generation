import operator

class CustomObject:
    def __init__(self, value):
        self.value = value

def find_max_by_attribute(obj_list, attr_name):
    if not obj_list:
        raise ValueError("Input list cannot be empty")
    
    return max(obj_list, key=operator.attrgetter(attr_name))

if __name__ == '__main__':
    objects = [CustomObject(5), CustomObject(3), CustomObject(9)]
    max_obj = find_max_by_attribute(objects, 'value')
    print(max_obj.value)