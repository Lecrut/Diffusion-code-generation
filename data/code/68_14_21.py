from typing import Iterable, TypeVar

T = TypeVar('T')

def symmetric_difference(iterable1: Iterable[T], iterable2: Iterable[T]) -> set[T]:
    def to_set(iterable: Iterable[T]) -> set[T]:
        return set(iterable)
    
    set1 = to_set(iterable1)
    set2 = to_set(iterable2)
    
    def compute_symmetric_difference(set1: set[T], set2: set[T]) -> set[T]:
        return (set1 - set2) | (set2 - set1)
    
    return compute_symmetric_difference(set1, set2)

if __name__ == '__main__':
    test_cases = {
        'case1': ([1, 2, 3, 4], [3, 4, 5, 6]),
        'case2': (['a', 'b', 'c'], ['b', 'c', 'd']),
        'case3': ({10, 20, 30}, {20, 30, 40}),
        'case4': ('hello', 'world')
    }
    
    for name, (iterable1, iterable2) in test_cases.items():
        result = symmetric_difference(iterable1, iterable2)
        print(f"{name}: {result}")