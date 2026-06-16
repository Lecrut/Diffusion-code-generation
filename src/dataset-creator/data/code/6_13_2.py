from typing import Any
class Comparator:
    def compare(self, value1: Any, value2: Any) -> bool:
        try:
            if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
                return value1 > value2
            elif isinstance(value1, str) and isinstance(value2, str):
                return value1 > value2
            else:
                raise TypeError("Unsupported types for comparison")
        except Exception as e:
            print(f"Error during comparison: {e}")
            return False
if __name__ == '__main__':
    comparator = Comparator()
    test_cases = [
        (10, 5),
        ("apple", "banana"),
        (3.14, 2.71),
        ([1], [2]),                                                                             
    ]
    for val1, val2 in test_cases:
        result = comparator.compare(val1, val2)
        print(f"{val1} > {val2}: {result}")