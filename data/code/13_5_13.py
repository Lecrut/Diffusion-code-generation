def fetch_field(obj, attr_name):
    if hasattr(obj, attr_name):
        return getattr(obj, attr_name)
    return None

class CustomObject:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

if __name__ == '__main__':
    obj = CustomObject(10, 20)
    print(fetch_field(obj, 'field1'))
    print(fetch_field(obj, 'nonexistent'))