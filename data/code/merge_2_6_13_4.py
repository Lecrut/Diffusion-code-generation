from typing import Any
class Comparator:
    def greater_than(self, a: Any, b: Any) -> bool | None:
        try:
            return a > b
        except TypeError:
            return None
        except Exception:
            return None
if __name__ == '__main__':
    comp = Comparator()
    test_cases = [
        (10, 5),                               
        ("apple", "banana"),                     
        ([1], [2]),                                                                                                                                                                
    ]
    results = []
    for val_a, val_b in test_cases:
        res = comp.greater_than(val_a, val_b)
        if res is not None:
            results.append((val_a, val_b, res))
        else:
            results.append((val_a, val_b, "Error"))
    for item in results:
        print(item)