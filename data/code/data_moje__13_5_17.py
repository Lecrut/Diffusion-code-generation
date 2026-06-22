def safe_get_field(obj, field_name):
    return getattr(obj, field_name, None)

class CustomObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

if __name__ == '__main__':
    obj = CustomObject("test", 42)
    print(safe_get_field(obj, "name"))
    print(safe_get_field(obj, "value"))
    print(safe_get_field(obj, "missing"))