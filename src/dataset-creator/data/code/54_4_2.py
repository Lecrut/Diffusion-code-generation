from typing import Sequence
def compute_center_mark(seq: Sequence) -> tuple[int | float]:
    if not seq:
        return (0.0,)
    n = len(seq)
    start_idx, end_idx = 0, n - 1
    center_index = n // 2 if n % 2 == 1 else (n // 2) + 1
    return (seq[center_index], seq[end_idx] * -1.0)
if __name__ == '__main__':
    sample_list: list[int] = [1, 2, 3, 4, 5]
    result = compute_center_mark(sample_list)
    print(result)