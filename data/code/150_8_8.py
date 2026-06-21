from typing import TypeVar, Sequence, List
T = TypeVar('T')

def remove_all_occurrences(sequence: Sequence[T], value: T) -> List[T]:
    return [item for item in sequence if item != value]
if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 2, 5]
    value_to_remove = 2
    result = remove_all_occurrences(sample_sequence, value_to_remove)
    print(result)