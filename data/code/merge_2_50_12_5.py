from typing import Union
def sum_three_variables(a: float, b: float, c: float) -> float:
    return a + b + c
if __name__ == '__main__':
    val1 = 10.5
    val2 = 20.75
    val3 = 30.25
    result = sum_three_variables(val1, val2, val3)
    print(result)