from typing import List, TypeVar
from collections.abc import Sequence

T = TypeVar('T')
_MIN_LENGTH = 2
_INDEX_OFFSET = 1

def get_second_last(data: Sequence[T]) -> T:
    if not isinstance(data, Sequence) or isinstance(data, str):
        raise TypeError("Input must be a sequence of elements")
    length = len(data)
    if length < _MIN_LENGTH:
        raise ValueError(f"Sequence must contain at least {_MIN_LENGTH} elements")
    return data[-_INDEX_OFFSET - 1]

if __name__ == '__main__':
    test_values = [100, 200, 300, 400, 500]
    output = get_second_last(test_values)
    print(output)
    tuple_data = ('a', 'b', 'c', 'd')
    output_tuple = get_second_last(tuple_data)
    print(output_tuple)