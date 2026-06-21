from typing import TypeVar, Sequence, List

T = TypeVar('T')

def remove_all_occurrences(seq: Sequence[T], value: T) -> List[T]:
    if not isinstance(seq, Sequence):
        raise ValueError("The first argument must be a sequence.")
    return [item for item in seq if item != value]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 2, 6]
    value_to_remove = 2
    result = remove_all_occurrences(sample_sequence, value_to_remove)
    print(result)