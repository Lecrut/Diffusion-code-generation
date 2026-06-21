from typing import TypeVar, Sequence, List

T = TypeVar('T')

def is_valid_sequence(seq: Sequence[T]) -> bool:
    return isinstance(seq, (list, tuple))

def remove_all_occurrences(seq: Sequence[T], value: T) -> List[T]:
    if not is_valid_sequence(seq):
        raise ValueError("Input must be a sequence")
    
    return [item for item in seq if item != value]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 2, 6]
    value_to_remove = 2
    result = remove_all_occurrences(sample_sequence, value_to_remove)
    print(result)