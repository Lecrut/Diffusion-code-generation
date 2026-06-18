import json
def deep_equality_check(a: any, b: any) -> bool:
    if type(a) != type(b):
        return False
    try:
        if isinstance(a, (list, tuple)):
            if len(a) != len(b):
                return False
            for i in range(len(a)):
                if not deep_equality_check(a[i], b[i]):
                    return False
            return True
        elif isinstance(a, dict):
            if set(a.keys()) != set(b.keys()):
                return False
            for key in a:
                if not deep_equality_check(a[key], b[key]):
                    return False
            return True
        else:
            return a == b
    except Exception:
        return False
if __name__ == '__main__':
    sample_a = {
        "id": 1,
        "items": [
            {"type": "apple", "qty": 5},
            {"type": "banana", "qty": 3}
        ],
        "nested": {
            "level1": ["a", "b"],
            "level2": None
        }
    }
    sample_b = {
        "id": 1,
        "items": [
            {"type": "apple", "qty": 5},
            {"type": "banana", "qty": 3}
        ],
        "nested": {
            "level1": ["a", "b"],
            "level2": None
        }
    }
    sample_c = {
        "id": 1,
        "items": [
            {"type": "apple", "qty": 5},
            {"type": "banana", "qty": 4}
        ],
        "nested": {
            "level1": ["a", "b"],
            "level2": None
        }
    }
    sample_d = [
        (1, 2),
        ("x", "y")
    ]
    result_a_b = deep_equality_check(sample_a, sample_b)
    result_a_c = deep_equality_check(sample_a, sample_c)
    result_abcd = deep_equality_check(sample_d, [
        (1, 2),
        ("x", "y")
    ])
    print(f"Sample A equals Sample B: {result_a_b}")
    print(f"Sample A equals Sample C: {result_a_c}")
    print(f"Tuples list equality check: {result_abcd}")