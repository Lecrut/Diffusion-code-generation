from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def count_from_start(sequence: Union[list[T], tuple[T, ...]]) -> int:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    return len(sequence)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b', 'c')
    result_1: int = count_from_start(sample_list)
    result_2: int = count_from_start(sample_tuple)
    print(f"List item count: {result_1}")
    print(f"Tuple item count: {result_2}")