from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def count_elements(iterable: Iterable[T]) -> int:
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c')
    count_from_list = count_elements(sample_list)
    count_from_tuple = count_elements(sample_tuple)
    print(f"List element count: {count_from_list}")
    print(f"Tuple element count: {count_from_tuple}")