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
    tuple1 = ('a', 'b', 'c')
    tuple2 = ('b', 'c', 'd')
    result = symmetric_difference(tuple1, tuple2)
    print(result)
    set1 = {10, 20, 30}
    set2 = {20, 30, 40}
    result = symmetric_difference(set1, set2)
    print(result)
    string1 = 'hello'
    string2 = 'world'
    result = symmetric_difference(string1, string2)
    print(result)