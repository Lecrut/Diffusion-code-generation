from typing import Sequence, TypeVar
T = TypeVar('T')
def element_wise_difference(seq1: Sequence[T], seq2: Sequence[T]) -> list[T]:
    result = []
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have equal length.")
    for i in range(len(seq1)):
        diff = seq1[i] - seq2[i]
        result.append(diff)
    return result
if __name__ == '__main__':
    a: list[int] = [5, 3, 8, 4]
    b: list[int] = [2, 7, 9, 10]
    diff_list: list[int] = element_wise_difference(a, b)
    print(diff_list)