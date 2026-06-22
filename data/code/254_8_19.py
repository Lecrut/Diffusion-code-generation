class CustomObject:
    def __init__(self, value):
        self.value = value

def find_min_by_attribute(obj_list, attr_name):
    if not obj_list:
        raise ValueError("Input list cannot be empty")
    
    min_obj = min(obj_list, key=lambda obj: getattr(obj, attr_name))
    return getattr(min_obj, attr_name)

if __name__ == '__main__':
    objects1 = [CustomObject(3.14), CustomObject(1.618), CustomObject(2.718)]
    objects2 = [CustomObject(10), CustomObject(-5), CustomObject(20.5), CustomObject(0)]
    objects3 = [CustomObject(5), CustomObject(5.0), CustomObject(4.99)]
    objects4 = [CustomObject(-100), CustomObject(0.5), CustomObject(-50.2)]

    print(f"Min value in {objects1}: {find_min_by_attribute(objects1, 'value')}")
    print(f"Min value in {objects2}: {find_min_by_attribute(objects2, 'value')}")
    print(f"Min value in {objects3}: {find_min_by_attribute(objects3, 'value')}")
    print(f"Min value in {objects4}: {find_min_by_attribute(objects4, 'value')}")