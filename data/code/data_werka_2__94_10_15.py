from typing import Sequence

PREDICATE_CHECKER = lambda item: item is True

def _validate_input(value, items):
    if not isinstance(value, bool):
        raise ValueError("First argument must be a boolean")
    if not isinstance(items, Sequence):
        raise ValueError("Second argument must be a sequence")
    for idx, item in enumerate(items):
        if not isinstance(item, bool):
            raise ValueError(f"Element at index {idx} is not a boolean")

def is_any_true(value, items):
    _validate_input(value, items)
    if value:
        return True
    for item in items:
        if PREDICATE_CHECKER(item):
            return True
    return False

if __name__ == '__main__':
    result1 = is_any_true(False, [False, False, True])
    print(result1)
    result2 = is_any_true(True, [False, False])
    print(result2)
    result3 = is_any_true(False, [False, False])
    print(result3)