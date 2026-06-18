def values_match(*args):
    if len(args) != 2:
        return False
    a, b = args
    try:
        type_a = type(a)
        type_b = type(b)
        is_immutable = isinstance(type_a, (type(int), type(float), type(str), tuple)) and not hasattr(type_a, '__dict__') or\
                       (isinstance(a, str) or isinstance(a, int) or isinstance(a, float) or isinstance(a, bool))
        if a.__class__.__name__ == b.__class__.__name__:
            return a is b
    except:
        pass
    try:
        return a == b
    except TypeError:
        return False
if __name__ == '__main__':
    print(values_match(5, 5))
    print(values_match("hello", "world"))
    print(values_match([1,2], [3,4]))
    print(values_match((1,), (1,)))