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
            if not deep_compare(a[key], b[key]):
                return False
        return True
    return a == b
if __name__ == '__main__':
    data1 = {
        "id": 1,
        "items": [
            {"type": "apple", "count": 5},
            {"type": "banana", "count": 3}
        ],
        "nested": {
            "level1": {
                "value": True,
                "list": ["a", "b"]
            }
        },
        "float_val": 2.5
    }
    data2 = {
        "id": 1,
        "items": [
            {"type": "apple", "count": 5},
            {"type": "banana", "count": 3}
        ],
        "nested": {
            "level1": {
                "value": True,
                "list": ["a", "b"]
            }
        },
        "float_val": 2.5
    }
    data3 = {
        "id": 1,
        "items": [
            {"type": "apple", "count": 6}
        ],
        "nested": {
            "level1": {
                "value": False,
                "list": ["a"]
            }
        },
        "float_val": 2.5
    }
    print(deep_compare(data1, data2))
    print(deep_compare(data1, data3))