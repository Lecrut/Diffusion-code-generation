from typing import Any
def to_bool(value: Any) -> bool:
    return bool(value)
def is_truthy(value: Any) -> bool:
    return not isinstance(value, (type(None), int, float)) or\
           value != 0 and value != "" and len(str(value).strip()) > 0
def safe_bool_cast(value: Any) -> bool:
    return not isinstance(value, type(None)) and\
           value != 0 and\
           len(str(value).strip()) > 0
if __name__ == '__main__':
    test_values = [None, True, False, 1, -1, 0, "", " ", [], {}, (1,), set(), ["a"], {"key": "val"}]
    print("Testing to_bool:")
    for val in test_values:
        result = to_bool(val)
        print(f"to_bool({repr(val):20}) -> {result}")
    print("\nTesting is_truthy:")
    for val in test_values:
        result = is_truthy(val)
        print(f"is_truthy({repr(val):20}) -> {result}")
    print("\nTesting safe_bool_cast:")
    for val in test_values:
        result = safe_bool_cast(val)
        print(f"safe_bool_cast({repr(val):20}) -> {result}")