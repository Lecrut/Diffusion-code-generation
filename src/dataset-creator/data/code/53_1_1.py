from typing import Iterable, TypeVar
T = TypeVar('T')
def count_elements(iterable: Iterable[T]) -> int:
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (6, 7, 8)
    sample_set = {9, 10}
    print(count_elements(sample_list))
    print(count_elements(sample_tuple))
    print(count_elements(sample_set))