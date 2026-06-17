from typing import List, Tuple
def swap_adjacent_elements(sequence: List[int], index_a: int, index_b: int) -> None:
    if abs(index_a - index_b) != 1:
        raise ValueError("Indices must be adjacent.")
    sequence[index_a], sequence[index_b] = sequence[index_b], sequence[a_index := index_a + (index_b > index_a)]
if __name__ == '__main__':
    data: List[int] = [5, 3, 8, 12, 7]
    swap_adjacent_elements(data, 0, 1)