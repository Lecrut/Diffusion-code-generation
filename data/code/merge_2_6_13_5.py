from typing import Any
class Comparator:
    def greater_than(self, a: Any, b: Any) -> bool:
        try:
            return a > b
        except TypeError as e:
            raise RuntimeError(f"Cannot compare {type(a).__name__} with {type(b).__name__}: {e}")
if __name__ == '__main__':
    comparator = Comparator()
    test_cases = [
        (10, 5),
        ("apple", "banana"),
        ([1, 2], [3]),
        ((True,), (False,)),
    ]
    for val_a, val_b in test_cases:
        result = comparator.greater_than(val_a, val_b)
        print(f"{val_a} > {val_b}: {result}")