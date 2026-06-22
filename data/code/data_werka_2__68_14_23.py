from typing import Iterable, TypeVar

T = TypeVar('T')

def symmetric_difference(iterable1: Iterable[T], iterable2: Iterable[T]) -> set[T]:
    def to_set(iterable: Iterable[T]) -> set[T]:
        return set(iterable)
    
    set1 = to_set(iterable1)
    set2 = to_set(iterable2)
    
    def diff(set_a: set[T], set_b: set[T]) -> set[T]:
        return set_a - set_b
    
    return diff(set1, set2) | diff(set2, set1)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    print(symmetric_difference(list1, list2))
    
    tuple1 = ('a', 'b', 'c')
    tuple2 = ('b', 'c', 'd')
    print(symmetric_difference(tuple1, tuple2))
    
    set1 = {10, 20, 30}
    set2 = {20, 30, 40}
    print(symmetric_difference(set1, set2))
    
    string1 = 'hello'
    string2 = 'world'
    print(symmetric_difference(string1, string2))