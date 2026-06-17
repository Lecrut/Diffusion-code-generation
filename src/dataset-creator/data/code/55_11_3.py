from typing import Sequence, TypeVar, List
T = TypeVar('T')
def swap_adjacent_elements(sequence: Sequence[T], index_a: int, index_b: int) -> None:
    if len(sequence) < 2:
        raise IndexError("Sequence must have at least two elements.")
    min_index = min(index_a, index_b)
    max_index = max(index_a, index_b)
    if not (0 <= min_index and max_index < len(sequence)):
        raise IndexError(f"Indices {index_a} or {index_b} are out of bounds for sequence length {len(sequence)}.")
    if abs(max_index - min_index) != 1:
        raise ValueError("Provided indices must be adjacent.")
    value_at_a = sequence[min_index]
    value_at_b = sequence[max_index]
    sequence[min_index], sequence[max_index] = value_at_b, value_at_a
if __name__ == '__main__':
    sample_list: List[int] = [10, 20, 30, 40, 50]
    swap_adjacent_elements(sample_list, 1, 2)
    print(f"Result after swapping indices 1 and 2: {sample_list}")