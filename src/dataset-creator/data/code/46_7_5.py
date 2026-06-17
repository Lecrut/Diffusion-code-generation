from typing import Sequence, TypeVar
T = TypeVar('T')
def element_wise_difference(seq1: Sequence[T], seq2: Sequence[T]) -> list[T]:
    result_list: list[T] = []
    if len(seq1) != len(seq2):
        raise ValueError("Both input sequences must have the same length.")
    for i in range(len(seq1)):
        diff_value = seq1[i] - seq2[i]
        result_list.append(diff_value)
    return result_list
if __name__ == '__main__':
    sample_seq_1: list[int] = [5, 3, 8, 4]
    sample_seq_2: list[int] = [2, 7, 1, 9]
    difference_result: list[int] = element_wise_difference(sample_seq_1, sample_seq_2)
    print(difference_result)