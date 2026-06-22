def get_field_safely(obj, field_name):
    if hasattr(obj, field_name):
        return getattr(obj, field_name)
    return None

class SampleObject:
    def __init__(self):
        self.name = "Alice"
        self.age = 30

if __name__ == '__main__':
    obj = SampleObject()
    print(get_field_safely(obj, "name"))
    print(get_field_safely(obj, "age"))
    print(get_field_safely(obj, "nonexistent"))