from typing import Any
class Comparator:
    def greater_than(self, value1: Any, value2: Any) -> bool | None:
        try:
            return value1 > value2
        except TypeError as e:
            print(f"Error during comparison: {e}")
            raise
if __name__ == '__main__':
    comparator = Comparator()
    test_cases = [
        (5, 3),                               
        ("apple", "banana"),                       
        ([1], [2]),                                 
        ((1,), (2,)),                                
    ]
    for val_a, val_b in test_cases:
        result = comparator.greater_than(val_a, val_b)
        print(f"{val_a} > {val_b}: {result}")