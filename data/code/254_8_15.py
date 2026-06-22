class CustomObject:
    def __init__(self, value):
        self.value = value

def find_min_by_attribute(obj_list, attr_name):
    if not obj_list:
        raise ValueError("Input list cannot be empty")
    
    min_obj = min(obj_list, key=lambda x: getattr(x, attr_name))
    return getattr(min_obj, attr_name)

if __name__ == '__main__':
    obj1 = CustomObject(3.14)
    obj2 = CustomObject(1.618)
    obj3 = CustomObject(2.718)
    
    list_of_objs = [obj1, obj2, obj3]
    
    print(f"Min value: {find_min_by_attribute(list_of_objs, 'value')}")