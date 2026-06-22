class CustomObject:
    def __init__(self, value):
        self.value = value

def find_min_by_attribute(obj_list, attr_name):
    return min(obj_list, key=lambda obj: getattr(obj, attr_name))

if __name__ == '__main__':
    objects = [CustomObject(5), CustomObject(3), CustomObject(9)]
    min_obj = find_min_by_attribute(objects, 'value')
    print(min_obj.value)