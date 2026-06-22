def safe_equals(obj1, obj2):
    if obj1 is None and obj2 is None:
        return True
    if obj1 is None or obj2 is None:
        return False
    return obj1 == obj2
if __name__ == '__main__':
    sample1 = None
    sample2 = None
    sample3 = 42
    sample4 = 'hello'
    print(safe_equals(sample1, sample2))
    print(safe_equals(sample1, sample3))
    print(safe_equals(sample3, sample3))
    print(safe_equals(sample4, 'hello'))
    print(safe_equals(sample4, None))