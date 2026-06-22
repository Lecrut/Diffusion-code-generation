def fetch_field_value(obj, attr_name):
    return getattr(obj, attr_name, None)

class SampleObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    obj = SampleObject("Alice", 30)
    print(fetch_field_value(obj, "name"))
    print(fetch_field_value(obj, "age"))
    print(fetch_field_value(obj, "nonexistent"))