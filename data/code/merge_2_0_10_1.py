def values_match(*args):
    if len(args) != 2:
        return False
    obj1, obj2 = args
    try:
        is_immutable = isinstance(obj1, (int, float, str, tuple)) and not hasattr(obj1, '__dict__')
        if is_immutable or type(obj1).__name__ in ('list', 'set'):
            return obj1 == obj2
        try:
            return obj1 == obj2
        except TypeError:
            return id(obj1) is id(obj2)
    except Exception:
        return False
if __name__ == '__main__':
    print(values_match(5, 5))
    print(values_match("hello", "world"))
    print(values_match([1, 2], [1, 3]))
    print(values_match({'a': 1}, {'b': 1}))
    print(values_match((1, 2), (1, 2)))