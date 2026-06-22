class CustomObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def safe_get_field(instance, field_name):
    try:
        return getattr(instance, field_name)
    except AttributeError:
        return None

if __name__ == '__main__':
    obj = CustomObject('test', 42)
    result_exists = safe_get_field(obj, 'name')
    result_missing = safe_get_field(obj, 'nonexistent')
    print(result_exists)
    print(result_missing)