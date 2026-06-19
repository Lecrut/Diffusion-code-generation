def safe_equals(obj1, obj2):
    if obj1 is None and obj2 is None:
        return True
    if obj1 is None or obj2 is None:
        return False
    return obj1 == obj2
if __name__ == '__main__':
    a = None
    b = 5
    c = 5
    d = None
    e = 'hello'
    f = 'world'
    print(safe_equals(a, b))
    print(safe_equals(b, c))
    print(safe_equals(a, d))
    print(safe_equals(e, f))