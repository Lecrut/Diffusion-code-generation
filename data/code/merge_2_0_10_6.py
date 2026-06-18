def values_match(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments are required.")
    a = args[0]
    b = args[1]
    try:
        type(a).__eq__
    except AttributeError:
        return False
    identity_match = id(a) == id(b)
    if not isinstance(type(a), type):
        return True
    immutable_types = (int, float, str, tuple, bytes, complex)
    if type(a) in immutable_types and type(b) in immutable_types:
        return a is b or identity_match
    try:
        result = a == b
        return bool(result)
    except TypeError:
        return False
if __name__ == '__main__':
    print(values_match(5, 5))
    print(values_match("hello", "world"))
    print(values_match([1, 2], [1, 2]))
    print(values_match((3,), (3,)))