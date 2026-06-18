def values_match(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments are required.")
    a = args[0]
    b = args[1]
    try:
        hash(a) and hash(b)
        return (a is b) or (type(a).__name__ == type(b).__name__ and a == b)
    except TypeError:
        pass
    if isinstance(a, dict):
        for key in set(a.keys()) | set(b.keys()):
            if not values_match(a[key], b.get(key)):
                return False
        return True
    elif isinstance(a, (list, tuple)) or hasattr(a, '__iter__'):
        try:
            iter_a = list(a)
            iter_b = list(b)
            for i in range(min(len(iter_a), len(iter_b))):
                if not values_match(iter_a[i], iter_b[i]):
                    return False
            return True
        except TypeError:
            pass
    try:
        hash(a) and hash(b)
        return a is b or (type(a).__name__ == type(b).__name__ and a == b)
    except TypeError:
        raise ValueError("Objects must be comparable.")
if __name__ == '__main__':
    print(values_match(5, 5))
    print(values_match([1, 2], [1, 2]))
    print(values_match({'a': 1}, {'a': 1}))
    print(values_match("hello", "world"))