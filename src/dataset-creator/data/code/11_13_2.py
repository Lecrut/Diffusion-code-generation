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
    elif isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        for key in a:
            if not deep_compare(a[key], b[key]):
                return False
        return True
    else:
        return a == b
if __name__ == '__main__':
    sample_a = {
        "id": 1,
        "items": [
            {"x": 5},
            {"y": [3.0, None]}
        ],
        "active": True
    }
    sample_b = {
        "id": 2,
        "items": [
            {"x": 6}
        ]
    }
    result_a = deep_compare(sample_a, sample_a)
    result_b = deep_compare(sample_a, sample_b)
    print(result_a and not result_b)