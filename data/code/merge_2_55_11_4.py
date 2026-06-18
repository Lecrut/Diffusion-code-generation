from typing import Sequence, TypeVar
T = TypeVar('T')
def swap_adjacent_indices(sequence: list[T], index1: int, index2: int) -> None:
    if not isinstance(sequence, list):
        raise TypeError("Sequence argument must be a list.")
    min_index = min(index1, index2)
    max_index = max(index1, index2)
    if abs(max_index - min_index) != 1:
        raise IndexError(f"Indices {index1} and {index2} are not adjacent.")
    if min_index < 0 or min_index >= len(sequence):
        raise IndexError("Index out of bounds for the sequence.")
    temp = sequence[min_index]
    sequence[min_index] = sequence[max_index]
    sequence[max_index] = temp
if __name__ == '__main__':
    sample_data: list[int] = [10, 20, 30, 40, 50]
    try:
        swap_adjacent_indices(sample_data, 1, 2)
        print(f"Swapped indices 1 and 2. Result: {sample_data}")
        sample_data_2 = [100, 200, 300, 400]
        swap_adjacent_indices(sample_data_2, -1, 0)
        print(f"Swapped indices -1 and 0. Result: {sample_data_2}")
    except (IndexError, TypeError) as e:
        print(f"An error occurred: {e}")