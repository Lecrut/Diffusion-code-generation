from typing import TypeVar, Sequence, List

T = TypeVar('T')

def remove_all_occurrences(seq: Sequence[T], value: T) -> List[T]:
    return [item for item in seq if item != value]

if __name__ == '__main__':
    sample_sequence = ['apple', 'banana', 'cherry', 'banana', 'date']
    value_to_remove = 'banana'
    result = remove_all_occurrences(sample_sequence, value_to_remove)
    print(result)