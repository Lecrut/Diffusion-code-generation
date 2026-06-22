class CustomObject:
    def __init__(self, value):
        self.value = value

def find_min_by_attribute(objects, attribute_name):
    if not objects:
        raise ValueError("Input list cannot be empty")
    
    min_object = min(objects, key=lambda obj: getattr(obj, attribute_name))
    return getattr(min_object, attribute_name)

if __name__ == '__main__':
    obj1 = CustomObject(3.14)
    obj2 = CustomObject(1.618)
    obj3 = CustomObject(2.718)
    list1 = [obj1, obj2, obj3]
    
    print(f"Min value: {find_min_by_attribute(list1, 'value')}")