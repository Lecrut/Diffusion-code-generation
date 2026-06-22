class CustomObject:
    def __init__(self, value):
        self.value = value

def find_min_by_attribute(data, attribute_name):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    min_obj = data[0]
    for obj in data:
        if getattr(obj, attribute_name) < getattr(min_obj, attribute_name):
            min_obj = obj
    
    return min_obj

if __name__ == '__main__':
    obj1 = CustomObject(3.14)
    obj2 = CustomObject(1.618)
    obj3 = CustomObject(2.718)
    sample_list = [obj1, obj2, obj3]
    
    min_obj = find_min_by_attribute(sample_list, 'value')
    print(f"Min value: {min_obj.value}")