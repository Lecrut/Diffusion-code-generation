class SafeObjectFetcher:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_field(self, field_name):
        return getattr(self, field_name, None)

if __name__ == '__main__':
    obj = SafeObjectFetcher(name="Alice", age=30, city="New York")
    print(obj.get_field("name"))
    print(obj.get_field("age"))
    print(obj.get_field("country"))