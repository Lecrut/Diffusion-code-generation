from typing import TypeVar, Sequence, Tuple
T = TypeVar('T')
def swap_elements(seq: Sequence[T], i1: int, i2: int) -> None:
    if not isinstance(i1, int):
        raise TypeError(f"Index must be an integer, got {type(i1).__name__}")
    if len(seq) <= max(abs(i1), abs(i2)):
        raise IndexError("Indices are out of bounds")
    seq[i1], seq[i2] = seq[i2], seq[i1]
if __name__ == '__main__':
    data: list[int] = [10, 30, 40, 50, 60]
    swap_elements(data, 1, 2)
    print(f"Result: {data}")