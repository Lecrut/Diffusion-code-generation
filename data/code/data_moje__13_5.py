def fetch_field_value(obj, attribute_name):
    return getattr(obj, attribute_name, None)

if __name__ == '__main__':
    class SampleObject:
        def __init__(self):
            self.name = "test"
            self.value = 42

    obj = SampleObject()
    print(fetch_field_value(obj, "name"))
    print(fetch_field_value(obj, "value"))
    print(fetch_field_value(obj, "missing"))