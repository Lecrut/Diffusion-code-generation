from typing import Union

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

if __name__ == '__main__':
    print(multiply(3, 4.5))
    print(multiply(2.5, 6))