from typing import List, Tuple
def swap_adjacent_elements(sequence: List[int], index_a: int, index_b: int) -> None:
    if abs(index_a - index_b) != 1:
        raise ValueError("Indices must be adjacent.")
    value = sequence[index_a]
    sequence[index_a] = sequence[index_b]
    sequence[index_b] = value
if __name__ == '__main__':
    data_list: List[int] = [5, 3, 8, 12, 7]
    swap_adjacent_elements(data_list, 0, 1)