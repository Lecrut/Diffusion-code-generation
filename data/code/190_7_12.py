from typing import Iterable

def value_exists(target: int, iterable: Iterable[int]) -> bool:
    return target in iterable
if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    print(value_exists(3, sample_iterable))
    print(value_exists(6, sample_iterable))