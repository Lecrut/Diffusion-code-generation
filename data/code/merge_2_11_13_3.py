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
            {"type": "apple", "count": 5},
            {"type": "banana", "count": 3}
        ],
        "nested": {
            "level_1": ["a", "b"],
            "level_2": [[1, 2], [3]]
        }
    }
    sample_b = {
        "id": 1,
        "items": [
            {"type": "apple", "count": 5},
            {"type": "banana", "count": 3}
        ],
        "nested": {
            "level_1": ["a", "b"],
            "level_2": [[1, 2], [3]]
        }
    }
    sample_c = {
        "id": 2,
        "items": [{"type": "orange"}]
    }
    print(deep_compare(sample_a, sample_b))
    print(deep_compare(sample_a, sample_c))