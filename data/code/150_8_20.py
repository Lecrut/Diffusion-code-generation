from typing import TypeVar, Sequence, List

T = TypeVar('T')

class GenericSequenceRemover:
    def remove_all_occurrences(self, seq: Sequence[T], value: T) -> List[T]:
        return [item for item in seq if item != value]

if __name__ == '__main__':
    remover = GenericSequenceRemover()
    sample_sequence = [1, 2, 3, 4, 5, 2, 6]
    value_to_remove = 2
    result = remover.remove_all_occurrences(sample_sequence, value_to_remove)
    print(result)

    another_sample = ['a', 'b', 'c', 'd', 'e', 'c']
    another_value_to_remove = 'c'
    another_result = remover.remove_all_occurrences(another_sample, another_value_to_remove)
    print(another_result)