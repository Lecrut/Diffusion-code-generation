def get_field_value(obj, field_name):
    try:
        return getattr(obj, field_name)
    except AttributeError:
        return None

if __name__ == '__main__':
    class Person:
        def __init__(self):
            self.name = "Alice"
            self.age = 30

    person = Person()
    print(get_field_value(person, "name"))
    print(get_field_value(person, "address"))