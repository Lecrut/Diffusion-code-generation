import inspect

class CustomObject:
    def __init__(self):
        self.name = "Sample"
        self.value = 42
        self.tags = ["a", "b"]

def fetch_field(obj, field_name):
    if hasattr(obj, field_name):
        return getattr(obj, field_name)
    return None

if __name__ == '__main__':
    obj = CustomObject()
    result1 = fetch_field(obj, "name")
    print(result1)
    result2 = fetch_field(obj, "missing_field")
    print(result2)
    result3 = fetch_field(obj, "value")
    print(result3)