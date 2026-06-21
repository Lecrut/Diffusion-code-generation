def fetch_field_value(obj, attr_name):
    return getattr(obj, attr_name, None)

if __name__ == '__main__':
    class CustomObject:
        def __init__(self):
            self.name = "test"
            self.value = 42

    obj = CustomObject()
    print(fetch_field_value(obj, "name"))
    print(fetch_field_value(obj, "value"))
    print(fetch_field_value(obj, "nonexistent"))