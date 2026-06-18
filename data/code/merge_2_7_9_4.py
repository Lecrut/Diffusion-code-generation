from typing import Any
def to_bool(value: Any) -> bool:
    return bool(value)
def is_truthy(value: Any) -> bool:
    return not (value is None or value == 0 or 
                isinstance(value, bool) and not value or 
                len(str(value)) == 0)
def safe_bool(value: Any, default: bool = True) -> bool:
    try:
        return bool(value)
    except Exception:
        return default
if __name__ == '__main__':
    test_cases = [0, 1, "", "hello", [], {}, None, True, False]
    print("Testing to_bool:")
    for case in test_cases:
        result = to_bool(case)
        print(f"to_bool({case!r}) -> {result}")
    print("\nTesting is_truthy:")
    for case in test_cases:
        result = is_truthy(case)
        print(f"is_truthy({case!r}) -> {result}")