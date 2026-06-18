from typing import Sequence, List, TypeVar
T = TypeVar('T')
def element_difference(seq1: Sequence[T], seq2: Sequence[T]) -> List[T]:
    result = []
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have equal length.")
    for i in range(len(seq1)):
        try:
            diff = seq1[i] - seq2[i]
            result.append(diff)
        except TypeError as e:
            raise ValueError(f"Elements at index {i} cannot be subtracted. Error details: {e}") from e
    return result
if __name__ == '__main__':
    sample_seq_a = [10, 20, 30]
    sample_seq_b = [5, 15, 25]
    difference_result = element_difference(sample_seq_a, sample_seq_b)
    print(difference_result)