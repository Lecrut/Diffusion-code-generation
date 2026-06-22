from typing import Tuple

def add_integers(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    sample_values: Tuple[int, int] = (3, 5)
    result = add_integers(*sample_values)
    print(result)