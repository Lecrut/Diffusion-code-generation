from typing import Union

def add(quantity1: int, quantity2: int) -> int:
    if not isinstance(quantity1, int) or not isinstance(quantity2, int):
        raise ValueError("Both arguments must be integers")
    return quantity1 + quantity2

if __name__ == '__main__':
    a = 10
    b = 5
    result = add(a, b)
    print(f"The sum of {a} and {b} is {result}")