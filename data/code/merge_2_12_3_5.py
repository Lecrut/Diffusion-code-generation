from typing import Any
def is_strict_odd_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and (value % 2 == 1 or value % 2 == -1)
if __name__ == '__main__':
    test_cases = [3, -5, 0, 4.5, "7", True]
    for case in test_cases:
        result = is_strict_odd_integer(case)
        print(f"{case!r}: {result}")