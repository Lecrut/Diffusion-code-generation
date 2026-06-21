import statistics
import math
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def get_median(sequence: Sequence[T]) -> T:
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    if n % 2 == 1:
        return sorted_seq[n // 2]
    else:
        mid1 = sorted_seq[n // 2 - 1]
        mid2 = sorted_seq[n // 2]
        if isinstance(mid1, float) or isinstance(mid2, float):
            return (mid1 + mid2) / 2
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    odd_list = [7, 1, 3, 5, 9]
    even_list = [10, 4, 6, 8]
    mixed_list = [1.5, 2.5, 3.5, 4.5]

    print(get_median(odd_list))
    print(get_median(even_list))
    print(get_median(mixed_list))