from typing import Union

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

if __name__ == '__main__':
    num1 = 6
    num2 = 7.5
    result = multiply(num1, num2)
    print(result)