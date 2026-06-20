from typing import Union

def validate_numbers(a: Union[int, float], b: Union[int, float]) -> bool:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return True

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    result1 = add_numbers(10, 5.5)
    print(f"The sum is {result1}")
    
    result2 = add_numbers(-3, 7)
    print(f"The sum is {result2}")