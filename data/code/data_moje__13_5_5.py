def fetch_field(obj, attr_name):
    if hasattr(obj, attr_name):
        return getattr(obj, attr_name)
    return None

class CustomObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    obj = CustomObject("Alice", 30)
    print(fetch_field(obj, "name"))
    print(fetch_field(obj, "age"))
    print(fetch_field(obj, "email"))
    print(fetch_field(obj, "address"))