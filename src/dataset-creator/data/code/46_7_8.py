from typing import Sequence, TypeVar
T = TypeVar('T')
def element_wise_difference(seq1: Sequence[T], seq2: Sequence[T]) -> list[T]:
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have equal length")
    result = []
    for i in range(len(seq1)):
        diff = seq1[i] - seq2[i]
        result.append(diff)
    return result
if __name__ == '__main__':
    a: list[int] = [3, 5, 7, 9]
    b: list[int] = [1, 4, 6, 8]
    diff_list = element_wise_difference(a, b)
    print(diff_list)