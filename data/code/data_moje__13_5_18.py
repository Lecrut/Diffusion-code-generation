def safe_get_attribute(obj, attr_name):
    return getattr(obj, attr_name, None)

class CustomObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

if __name__ == '__main__':
    obj = CustomObject("test", 42)
    print(safe_get_attribute(obj, "name"))
    print(safe_get_attribute(obj, "value"))
    print(safe_get_attribute(obj, "missing"))