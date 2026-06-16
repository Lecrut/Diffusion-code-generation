from typing import Any
class Comparator:
    def greater_than(self, a: Any, b: Any) -> bool | None:
        try:
            return a > b
        except TypeError as e:
            print(f"Comparison failed due to type mismatch: {e}")
            return None
if __name__ == '__main__':
    comp = Comparator()
    test_cases = [
        (10, 5),                               
        ("apple", "banana"),                      
        ([1, 2], [3]),                              
        (None, None),                           
    ]
    for val_a, val_b in test_cases:
        result = comp.greater_than(val_a, val_b)
        if result is not None:
            print(f"{val_a} > {val_b}: {result}")