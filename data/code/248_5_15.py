from typing import Tuple
NUM1: int = 3
NUM2: int = 5

def add_integers(a: int, b: int) -> int:
    return a + b
if __name__ == '__main__':
    result: int = add_integers(NUM1, NUM2)
    print(result)