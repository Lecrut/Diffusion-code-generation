def safe_fetch_attribute(obj, attr_name):
    try:
        return getattr(obj, attr_name)
    except AttributeError:
        return None

class CustomObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    obj = CustomObject("Alice", 30)
    print(safe_fetch_attribute(obj, "name"))
    print(safe_fetch_attribute(obj, "nonexistent"))