def get_field(obj, field_name):
    return getattr(obj, field_name, None)

class SampleObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    obj = SampleObject("Alice", 30)
    print(get_field(obj, "name"))
    print(get_field(obj, "age"))
    print(get_field(obj, "email"))
    print(get_field(obj, "city"))