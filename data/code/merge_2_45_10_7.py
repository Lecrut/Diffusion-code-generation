from typing import Union
def calculate_sum(a: float, b: float) -> float:
    return a + b
if __name__ == '__main__':
    try:
        num1 = 5.0
        num2 = 3.0
        result = calculate_sum(num1, num2)
        print(f"The sum is {result}")
    except TypeError as e:
        print("Error:", type(e).__name__, "occurred")