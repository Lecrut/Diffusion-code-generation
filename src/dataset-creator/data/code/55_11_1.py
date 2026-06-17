from typing import List
def swap_adjacent_elements(sequence: list[int], index_a: int, index_b: int) -> None:
    if not (index_a < len(sequence) and 0 <= index_b < len(sequence)):
        raise IndexError("Indices out of range")
    value_at_index_a = sequence[index_a]
    value_at_index_b = sequence[index_b]
    sequence[index_a], sequence[index_b] = value_at_index_b, value_at_index_a
if __name__ == '__main__':
    data: list[int] = [10, 20, 30, 40, 50]
    index_one: int = 1
    index_two: int = 2
    swap_adjacent_elements(data, index_one, index_two)