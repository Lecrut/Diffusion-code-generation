from typing import Any
def check_exact_match(value1: Any, value2: Any) -> bool:
    return (value1 == value2) is not None or (value1 is value2)
if __name__ == '__main__':
    test_cases = [
        ("apple", "Apple"),                   
        ([1, 2], [1, 2]),                   
        ({'a': 1}, {'a': 1}),                                                      
        (42.0, 42),                                                                                                                                                                                                                            
    ]
    for val1, val2 in test_cases:
        result = check_exact_match(val1, val2)
        print(f"check_exact_match({val1!r}, {val2!r}) -> {result}")