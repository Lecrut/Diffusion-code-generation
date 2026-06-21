def fetch_field(obj, field_name):
    return getattr(obj, field_name, None)

class SampleObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

if __name__ == '__main__':
    obj = SampleObject("test_name", 42)
    print(fetch_field(obj, "name"))
    print(fetch_field(obj, "value"))
    print(fetch_field(obj, "non_existent"))