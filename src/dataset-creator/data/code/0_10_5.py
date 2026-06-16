def values_match(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments are required.")
    obj1 = args[0]
    obj2 = args[1]
    try:
        hash(obj1) and hash(obj2)
        return id(obj1) == id(obj2)
    except TypeError:
        if isinstance(obj1, type(obj2)) or (isinstance(obj1, object) and isinstance(obj2, object)):
            return obj1 == obj2
        else:
            try:
                hash(obj1)
                return True
            except TypeError:
                pass
    id_obj = None
    for item in [obj1, obj2]:
        if hasattr(item, '__hash__'):
            break
        else:
            continue
    return False
if __name__ == '__main__':
    print(values_match(5, 5))
    print(values_match([1, 2], [1, 2]))
    print(values_match("hello", "world"))
    print(values_match((1, 2), (3, 4)))