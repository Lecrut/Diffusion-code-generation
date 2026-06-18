from typing import Sequence, TypeVar
T = TypeVar('T')
def swap_adjacent_elements(sequence: list[T], index_a: int, index_b: int) -> None:
    if not isinstance(sequence, list):
        raise TypeError("Input must be a mutable sequence (list).")
    min_index = min(index_a, index_b)
    max_index = max(index_a, index_b)
    if abs(max_index - min_index) != 1:
        raise IndexError(f"Indices {index_a} and {index_b} are not adjacent.")
    sequence[min_index], sequence[max_index] = (sequence[max_index], sequence[min_index])
if __name__ == '__main__':
    sample_data: list[int] = [10, 20, 30, 40, 50]
    try:
        swap_adjacent_elements(sample_data, 1, 2)
        print(f"Swapped elements at indices 1 and 2.")
        print("Result:", sample_data)
        large_dataset = list(range(1_000_000))
        swap_adjacent_elements(large_dataset, 500_000, 500_001)
        print(f"Large dataset swapped successfully. First element: {large_dataset[0]}, Last element: {large_dataset[-1]}")
    except (IndexError, TypeError) as e:
        print(f"An error occurred during swapping: {e}")