from typing import TypeVar, Sequence, Any
T = TypeVar('T')
def get_first_element(sequence: Sequence[T]) -> T:
    return next(iter(sequence), None)
if __name__ == '__main__':
    sample_list: list[int] = [10, 20, 30]
    sample_tuple: tuple[str, ...] = ('a', 'b', 'c')
    result_int: int | None = get_first_element(sample_list)
    result_str: str | None = get_first_element(sample_tuple)
    print(result_int)
    print(result_str)