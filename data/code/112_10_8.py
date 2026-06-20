from typing import Union

NUM1: int = 15
NUM2: int = 27

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

if __name__ == '__main__':
    print(add_numbers(NUM1, NUM2))