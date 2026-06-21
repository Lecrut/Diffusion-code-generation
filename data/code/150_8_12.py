from typing import TypeVar, Sequence, List

T = TypeVar('T')

def is_not_value(item: T, value: T) -> bool:
    return item != value

def remove_all_occurrences(seq: Sequence[T], value: T) -> List[T]:
    if not isinstance(seq, Sequence):
        raise TypeError("The first argument must be a sequence.")
    if seq and not all(isinstance(item, type(next(iter(seq)))) for item in seq):
        raise ValueError("All elements in the sequence must be of the same type.")
    
    return [item for item in seq if is_not_value(item, value)]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 2, 6]
    value_to_remove = 2
    result = remove_all_occurrences(sample_sequence, value_to_remove)
    print(result)