from typing import Sequence, TypeVar
T = TypeVar('T')
def get_last_item(sequence: Sequence[T]) -> T | None:
    return sequence[-1] if sequence else None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result: int | None = get_last_item(sample_list)
    print(result)
    empty_tuple: tuple[int, ...] = ()
    last_empty: int | None = get_last_item(empty_tuple)
    print(last_empty)