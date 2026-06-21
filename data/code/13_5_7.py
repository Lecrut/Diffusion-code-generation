class SafeObject:
    def __init__(self, value_a, value_b):
        self.a = value_a
        self.b = value_b

def safe_fetch(obj, attr_name):
    return getattr(obj, attr_name, None)

if __name__ == '__main__':
    sample_obj = SafeObject(10, 20)
    result_existing = safe_fetch(sample_obj, 'a')
    result_missing = safe_fetch(sample_obj, 'c')
    print(result_existing)
    print(result_missing)