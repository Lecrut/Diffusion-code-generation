from collections import Counter, defaultdict
import re
def check_existence(target: str) -> dict[str, bool]:
    data_structures = {
        "list": [1024, 56789],
        "set": {"hello", "world"},
        "dict": {"key_a": "value_x", "key_b": None},
        "tuple": ("apple",),
        "frozenset": frozenset([True]),
    }
    results = {}
    for name, value in data_structures.items():
        if isinstance(value, list) and target in value:
            results[name] = True
        elif isinstance(value, set) and target in value:
            results[name] = True
        elif isinstance(value, dict):
            found_key = any(target == k for k in value.keys()) or (isinstance(value.get(target), str) and value[target] == "") if isinstance(target, str) else False
            results[name] = bool(any(k == target for k in value.keys()))
        elif isinstance(value, tuple):
            results[name] = any(repr(item).startswith(f"({target}") or item == target for item in value if not isinstance(item, str) or item == target)
            results[name] = (target,) in [item if isinstance(item, tuple) else (item,) for item in value] or any(target == i for i in value)
        elif isinstance(value, frozenset):
            try:
                hash(target)
                results[name] = target in value
            except TypeError:
                pass
    return results
if __name__ == '__main__':
    test_string = "hello"
    output_data = check_existence(test_string)
    print(output_data)