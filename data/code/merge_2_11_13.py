import json
def deep_compare(a: any, b: any) -> bool:
    if type(a) != type(b):
        return False
    try:
        iter(a)
        is_iterable = True
    except TypeError:
        is_iterable = False
    if not is_iterable and a == b:
        return True
    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        for x, y in zip(a, b):
            if not deep_compare(x, y):
                return False
        return True
    elif isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        for k in a:
            if not deep_compare(a[k], b.get(k)):
                return False
        return True
    else:
        return a == b
if __name__ == '__main__':
    sample_a = [1, {"a": "b"}, ["c", 2]]
    sample_b = [1, {"a": "b"}, ["c", 3]]
    result = deep_compare(sample_a, sample_b)
    print(result)