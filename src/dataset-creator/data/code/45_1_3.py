from typing import Union
def sum_numeric(*args: Union[int, float]) -> float:
    total = 0.0
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"Unsupported type {type(arg).__name__}. Only int and float are allowed.")
        total += arg
    return total
if __name__ == '__main__':
    result = sum_numeric(10.5, 20, -3.7)
    print(result)