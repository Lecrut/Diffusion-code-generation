import operator

class CustomObject:

    def __init__(self, value):
        self.value = value

def find_max_by_attribute(obj_list, attr_name):
    return max(obj_list, key=operator.attrgetter(attr_name))
if __name__ == '__main__':
    obj1 = CustomObject(10)
    obj2 = CustomObject(5)
    obj3 = CustomObject(20)
    sample_list = [obj1, obj2, obj3]
    max_obj = find_max_by_attribute(sample_list, 'value')
    print(max_obj.value)