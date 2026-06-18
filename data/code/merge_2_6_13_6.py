from typing import Any
class GenericComparator:
    def __init__(self) -> None:
        pass
    @staticmethod
    def compare(value_a: Any, value_b: Any) -> bool:
        try:
            if type(value_a) != type(value_b):
                raise TypeError("Types must be identical for comparison.")
            return value_a > value_b
        except Exception as e:                
            print(f"Comparison error occurred: {e}")
            return False
if __name__ == '__main__':
    comparator = GenericComparator()
    test_cases = [
        (5, 3),
        ("apple", "banana"),
        ([1, 2], [1, 2, 3]),
        ({'a': 1}, {'b': 2}),
    ]
    for val_a, val_b in test_cases:
        result = comparator.compare(val_a, val_b)
        print(f"{val_a} > {val_b}: {result}")