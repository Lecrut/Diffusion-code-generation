from typing import Sequence, TypeVar
T = TypeVar('T')
def get_last_item(sequence: Sequence[T]) -> T | None:
    return sequence[-1] if len(sequence) > 0 else None
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'apple', True]
    result: int | str | bool | list[int] | None = get_last_item(sample_list)
    print(result)