from typing import Any
def is_strict_odd_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and (value % 2 == 1 or value % 2 == -1)
if __name__ == '__main__':
    test_values = [3, 4, -5, "odd", True, float(3.0), None]
    for val in test_values:
        result = is_strict_odd_integer(val)
        print(f"is_strict_odd_integer({val!r}) -> {result}")