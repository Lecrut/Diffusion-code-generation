from typing import TypeVar, Sequence, List

T = TypeVar('T')

class SequenceCleaner:
    @staticmethod
    def remove_all_occurrences(seq: Sequence[T], value: T) -> List[T]:
        return [item for item in seq if item != value]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 2, 6]
    value_to_remove = 2
    cleaned_sequence = SequenceCleaner.remove_all_occurrences(sample_sequence, value_to_remove)
    print(cleaned_sequence)