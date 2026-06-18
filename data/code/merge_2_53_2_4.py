from typing import Any, Iterable, TypeVar
T = TypeVar('T')
def count_from_start(sequence: Iterable[T]) -> int:
    if not isinstance(sequence, (str, list, tuple, set)):
        raise TypeError(f"Expected an iterable sequence type but got {type(sequence).__name__}")
    return len(sequence)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b')
    result_list = count_from_start(sample_list)
    result_tuple = count_from_start(sample_tuple)
    print(f"Count from start for list: {result_list}")
    print(f"Count from start for tuple: {result_tuple}")