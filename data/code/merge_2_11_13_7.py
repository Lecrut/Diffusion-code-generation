import json
def deep_compare(a: any, b: any) -> bool:
    if type(a) != type(b):
        return False
    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        if not all(deep_compare(x, y) for x, y in zip(a, b)):
            return False
    elif isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        if not all(deep_compare(a[k], b[k]) for k in a):
            return False
    else:
        if a != b:
            return False
    return True
if __name__ == '__main__':
    sample_a = [1, {"key": "value", "nested": [2, 3]}, (4,)]
    sample_b = [1, {"key": "value", "nested": [2, 3]}, (4,)]
    result = deep_compare(sample_a, sample_b)
    print(result)