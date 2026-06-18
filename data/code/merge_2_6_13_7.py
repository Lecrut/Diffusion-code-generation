from typing import Any
class Comparator:
    def is_greater(self, a: Any, b: Any) -> bool:
        try:
            return a > b
        except TypeError as e:
            raise ValueError(f"Cannot compare values of different types: {type(a)} and {type(b)}. Error details: {e}")
if __name__ == '__main__':
    comparator = Comparator()
    test_cases = [
        (10, 5),
        ("apple", "banana"),
        ([1, 2], [3]),
        ((True,), (False,)),
    ]
    for val_a, val_b in test_cases:
        try:
            result = comparator.is_greater(val_a, val_b)
            print(f"{val_a} > {val_b}: {result}")
        except ValueError as ve:
            print(f"Error comparing {val_a} and {val_b}: {ve}")
    invalid_comparison_cases = [
        ("hello", 123),
        ([], {}),
    ]
    for val_a, val_b in invalid_comparison_cases:
        try:
            result = comparator.is_greater(val_a, val_b)
            print(f"{val_a} > {val_b}: {result}")
        except ValueError as ve:
            print(f"Error comparing {val_a} and {val_b}: {ve}")