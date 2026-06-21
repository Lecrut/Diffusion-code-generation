def get_field_value(obj, attr_name):
    return getattr(obj, attr_name, None)

class CustomObject:
    def __init__(self):
        self.name = "Alice"
        self.age = 30

if __name__ == '__main__':
    obj = CustomObject()
    print(get_field_value(obj, "name"))
    print(get_field_value(obj, "age"))
    print(get_field_value(obj, "nonexistent"))