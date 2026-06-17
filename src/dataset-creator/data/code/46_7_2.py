from typing import Sequence, TypeVar
T = TypeVar('T')
def element_wise_difference(seq1: Sequence[T], seq2: Sequence[T]) -> list[T]:
    result = []
    min_len = min(len(seq1), len(seq2))
    for i in range(min_len):
        diff = seq1[i] - seq2[i]
        result.append(diff)
    return result
if __name__ == '__main__':
    sample_seq_1: list[int] = [5, 3, 8, 4]
    sample_seq_2: list[int] = [2, 7, 1, 9]
    difference_result = element_wise_difference(sample_seq_1, sample_seq_2)
    print(difference_result)