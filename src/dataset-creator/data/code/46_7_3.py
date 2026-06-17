from typing import Sequence, TypeVar
T = TypeVar('T')
def element_wise_difference(seq1: Sequence[T], seq2: Sequence[T]) -> list[T]:
    return [x - y for x, y in zip(seq1, seq2)]
if __name__ == '__main__':
    sample_seq_1 = [5.0, 10.0, 3.0]
    sample_seq_2 = [2.0, 7.0, 4.0]
    result = element_wise_difference(sample_seq_1, sample_seq_2)
    print(result)