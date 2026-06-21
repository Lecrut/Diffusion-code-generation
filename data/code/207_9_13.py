import operator

class CustomObject:
    def __init__(self, value):
        self.value = value

def find_max_by_attribute(obj_list, attr_name):
    return max(obj_list, key=operator.attrgetter(attr_name))

if __name__ == '__main__':
    objects = [CustomObject(10), CustomObject(20), CustomObject(5)]
    max_object = find_max_by_attribute(objects, 'value')
    print(max_object.value)