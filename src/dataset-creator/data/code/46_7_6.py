from typing import Sequence, TypeVar
T = TypeVar('T')
def element_wise_difference(seq1: Sequence[T], seq2: Sequence[T]) -> list[T]:
    try:
        return [a - b for a, b in zip(seq1, seq2)]
    except Exception as e:
        raise TypeError(f"Elements must support subtraction and have compatible types.") from e
if __name__ == '__main__':
    sample_list_a = [30.5, 40.6, 78.9]
    sample_list_b = [21.0, 40.0, 10.0]
    result: list[float] = element_wise_difference(sample_list_a, sample_list_b)
    print(result)