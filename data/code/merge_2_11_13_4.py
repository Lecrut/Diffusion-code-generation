import json
def deep_compare(a: any, b: any) -> bool:
    if type(a) != type(b):
        return False
    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not deep_compare(a[i], b[i]):
                return False
        return True
    if isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        for key in a:
            if not deep_compare(a[key], b.get(key)):
                return False
        return True
    return a == b
if __name__ == '__main__':
    data_a = {"user": [1, 2, "Alice"], "meta": {"id": 42}}
    data_b = {"user": [1, 2, "Alice"], "meta": {"id": 42}}
    data_c = {"user": [1, 3, "Bob"], "meta": {"id": 42}}
    result_a_b = deep_compare(data_a, data_b)
    result_a_c = deep_compare(data_a, data_c)
    print(result_a_b and not result_a_c)