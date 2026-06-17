from typing import Union
def calculate_sum(a: float, b: float) -> None:
    try:
        result = a + b
        print(f"Sum is {result}")
    except TypeError as e:
        raise ValueError("Both inputs must be numeric.") from e
if __name__ == '__main__':
    calculate_sum(10.5, 20.3)