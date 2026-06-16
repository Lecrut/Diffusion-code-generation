from typing import Any
class Comparator:
    def greater_than(self, a: Any, b: Any) -> bool | None:
        try:
            result = a > b
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return result
            return bool(result)
        except TypeError as e:
            raise type(e)(f"Cannot compare {type(a).__name__} with {type(b).__name__}: {e}")
if __name__ == '__main__':
    comparator = Comparator()
    test_cases = [
        (10, 5),                              
        ("apple", "banana"),                    
        ([1], [2]),                                                      
        (3.14, 3.14),                               
    ]
    for val_a, val_b in test_cases:
        try:
            result = comparator.greater_than(val_a, val_b)
            print(f"{val_a} > {val_b}: {result}")
        except TypeError as e:
            print(f"Error comparing {val_a} and {val_b}: {e}")