from typing import Union

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

if __name__ == '__main__':
    print(add_numbers(10, 20))
    print(add_numbers(5.5, 4.5))