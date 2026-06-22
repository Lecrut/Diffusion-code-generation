def safe_equals(obj1, obj2):
    if obj1 is None or obj2 is None:
        return obj1 is obj2
    return obj1 == obj2
if __name__ == '__main__':
    a = 5
    b = 5
    c = None
    d = None
    e = 10
    print(safe_equals(a, b))
    print(safe_equals(c, d))
    print(safe_equals(a, c))
    print(safe_equals(e, b))