from typing import Union

def add(quantity1: Union[int, float], quantity2: Union[int, float]) -> Union[int, float]:
    return quantity1 + quantity2

if __name__ == '__main__':
    a = 10
    b = 5.5
    result = add(a, b)
    print(f"The sum of {a} and {b} is: {result}")