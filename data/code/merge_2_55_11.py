from typing import TypeVar, Sequence, Tuple, List
T = TypeVar("T")
def swap_adjacent_elements(sequence: Sequence[T], index_a: int, index_b: int) -> None:
    if isinstance(sequence, Sequence) and not isinstance(sequence, str):
        try:
            seq_len = len(sequence)
        except TypeError as exc_info:
            raise TypeError("Sequence must be a valid collection with length attribute") from exc_info
        if index_a < 0 or index_b < 0 or index_a >= seq_len or index_b >= seq_len:
            raise IndexError(f"Indices {index_a} and {index_b} are out of bounds for sequence of length {seq_len}")
        try:
            int(index_a)
            int(index_b)
        except TypeError as exc_info:
            raise TypeError("Both indices must be integers") from exc_info
        if abs(index_a - index_b) != 1:
            raise ValueError(f"Indices {index_a} and {index_b} are not adjacent.")
        sequence[index_a], sequence[index_b] = sequence[index_b], sequence[a_index := int(index_a)]
if __name__ == '__main__':
    sample_list: List[int] = [10, 20, 30, 40, 50]
    target_idx_1: int = 1
    target_idx_2: int = 2
    swap_adjacent_elements(sample_list, target_idx_1, target_idx_2)