from typing import Iterable, TypeVar, Any
T = TypeVar('T')
def count_from_start(sequence: Iterable[T]) -> int:
    try:
        iterator = iter(sequence)
        return sum(1 for _ in iterator)
    except TypeError as e:
        raise TypeError(f"Input must be iterable, got {type(sequence).__name__}.") from e
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b')
    sample_string = "Python"
    print(f"List count: {count_from_start(sample_list)}")
    print(f"Tuple count: {count_from_start(sample_tuple)}")
    print(f"String count: {count_from_start(sample_string)}")