def safe_equals(obj1, obj2):
    if obj1 is None and obj2 is None:
        return True
    if obj1 is None or obj2 is None:
        return False
    return obj1 == obj2
if __name__ == '__main__':
    print(safe_equals(None, None))
    print(safe_equals(None, 5))
    print(safe_equals(5, None))
    print(safe_equals(5, 5))
    print(safe_equals('a', 'a'))
    print(safe_equals('a', 'b'))