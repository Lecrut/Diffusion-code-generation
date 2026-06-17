from typing import Sequence, TypeVar
T = TypeVar("T")
def swap_adjacent_indices(sequence: list[T], index_a: int, index_b: int) -> None:
    if isinstance(index_a, int) and isinstance(index_b, int):
        length = len(sequence)
        min_index = min(index_a, index_b)
        max_index = max(index_a, index_b)
        if 0 <= min_index < length:
            if not (max_index == min_index + 1 or max_index == min_index - 1):
                raise IndexError("Indices must be adjacent.")
            sequence[min_index], sequence[max_index] = sequence[max_index], sequence[min_index]
if __name__ == '__main__':
    sample_data: list[int] = [10, 20, 30, 40, 50]
    swap_adjacent_indices(sample_data, 1, 2)
    print(f"Original data type check: {type(sample_data)}")
    print("Data after swapping indices 1 and 2:", sample_data)