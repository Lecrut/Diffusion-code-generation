from typing import List, Sequence
def element_wise_difference(seq1: Sequence[float], seq2: Sequence[float]) -> List[float]:
    if len(seq1) != len(seq2):
        raise ValueError("Both input sequences must have the same length.")
    result = []
    for i, a in enumerate(seq1):
        b = seq2[i]
        diff = float(a - b)
        result.append(diff)
    return result
if __name__ == '__main__':
    sample_seq_1: Sequence[float] = [5.0, 3.0, 9.0, 7.0]
    sample_seq_2: Sequence[float] = [1.0, 4.0, 6.0, 8.0]
    difference_result: List[float] = element_wise_difference(sample_seq_1, sample_seq_2)
    print(difference_result)