def safe_get_attribute(obj, attr_name, default=None):
    if not hasattr(obj, attr_name):
        return default
    return getattr(obj, attr_name)

class SampleObject:
    def __init__(self):
        self.existing_field = "value123"

if __name__ == '__main__':
    sample = SampleObject()
    result1 = safe_get_attribute(sample, 'existing_field')
    result2 = safe_get_attribute(sample, 'nonexistent_field', 'default_value')
    print(result1)
    print(result2)