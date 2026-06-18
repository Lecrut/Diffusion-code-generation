from typing import Sequence, TypeVar
T = TypeVar('T')
def get_item_at_index(sequence: Sequence[T], index: int) -> T:
    return sequence[index]
if __name__ == '__main__':
    sample_list: list[int] = [10, 20, 30, 40, 50]
    sample_tuple: tuple[str, ...] = ('a', 'b', 'c')
    result_int: int = get_item_at_index(sample_list, 2)
    result_str: str = get_item_at_index(sample_tuple, 1)
    print(result_int)
    print(result_str)