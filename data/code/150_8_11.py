from typing import TypeVar, Sequence, List

T = TypeVar('T')

class SequenceCleaner:
    def remove_all_occurrences(self, seq: Sequence[T], value: T) -> List[T]:
        return [item for item in seq if item != value]

if __name__ == '__main__':
    cleaner = SequenceCleaner()
    sample_sequence_ints = [1, 2, 3, 4, 5, 2, 6]
    value_to_remove_ints = 2
    result_ints = cleaner.remove_all_occurrences(sample_sequence_ints, value_to_remove_ints)
    print(result_ints)

    sample_sequence_strs = ['a', 'b', 'c', 'd', 'e', 'c']
    value_to_remove_strs = 'c'
    result_strs = cleaner.remove_all_occurrences(sample_sequence_strs, value_to_remove_strs)
    print(result_strs)