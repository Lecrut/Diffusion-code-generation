class CustomObject:
    def __init__(self, value):
        self.value = value

def find_min_by_attribute(data, attr_name):
    if not data:
        raise ValueError("Input list cannot be empty")
    min_item = min(data, key=lambda x: getattr(x, attr_name))
    return getattr(min_item, attr_name)

if __name__ == '__main__':
    obj1 = CustomObject(3.14)
    obj2 = CustomObject(1.618)
    obj3 = CustomObject(2.718)
    list1 = [obj1, obj2, obj3]
    
    obj4 = CustomObject(10)
    obj5 = CustomObject(-5)
    obj6 = CustomObject(20.5)
    list2 = [obj4, obj5, obj6]
    
    print(f"Min value in {list1}: {find_min_by_attribute(list1, 'value')}")
    print(f"Min value in {list2}: {find_min_by_attribute(list2, 'value')}")