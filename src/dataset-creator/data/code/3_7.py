from typing import Union
def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
if __name__ == '__main__':
    result1 = divide(10, 2)
    print(f"10 / 2 = {result1}")
    result2 = divide(15, 3)
    print(f"15 / 3 = {result2}")
    result3 = divide(7, 2)
    print(f"7 / 2 = {result3}")
    try:
        result4 = divide(5, 0)
        print(f"5 / 0 = {result4}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")