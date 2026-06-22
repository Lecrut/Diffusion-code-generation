from typing import Iterable, TypeVar
T = TypeVar('T')

def symmetric_difference(iterable1: Iterable[T], iterable2: Iterable[T]) -> set[T]:
    set1 = set(iterable1)
    set2 = set(iterable2)
    return set1 - set2 | set2 - set1
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = symmetric_difference(list1, list2)
    print(result)