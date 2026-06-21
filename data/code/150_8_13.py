from typing import TypeVar, Sequence, List

T = TypeVar('T')

def remove_all_occurrences(seq: Sequence[T], value: T) -> List[T]:
    filtered_seq = [item for item in seq if item != value]
    return filtered_seq

if __name__ == '__main__':
    sample_sequence = ['apple', 'banana', 'cherry', 'apple']
    value_to_remove = 'apple'
    result = remove_all_occurrences(sample_sequence, value_to_remove)
    print(result)