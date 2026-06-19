from typing import Tuple

def compute_length_ratio(tuple1: Tuple, tuple2: Tuple) -> float:
    length1 = len(tuple1)
    length2 = len(tuple2)
    if length2 == 0:
        return float('inf')
    return length1 / length2

if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4, 5)
    sample_tuple2 = (6, 7, 8)
    ratio = compute_length_ratio(sample_tuple1, sample_tuple2)
    print(ratio)