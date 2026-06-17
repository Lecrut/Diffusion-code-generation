from typing import Iterable, TypeVar, Any
T = TypeVar('T')
def count_from_start(sequence: Iterable[T]) -> int:
    if not isinstance(sequence, (list, tuple, str)):
        raise TypeError(f"Expected an iterable input but received {type(sequence).__name__}")
    return len(sequence)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b')
    sample_string = "Python"
    print(f"List count: {count_from_start(sample_list)}")
    print(f"Tuple count: {count_from_start(sample_tuple)}")
    print(f"String count: {count_from_start(sample_string)}")