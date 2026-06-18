from typing import Iterable, TypeVar
T = TypeVar('T')
def get_first_element(iterable: Iterable[T]) -> T | None:
    try:
        return next(iter(iterable))
    except StopIteration:
        return None
if __name__ == '__main__':
    sample_list: list[int] = [10, 20, 30]
    first_item: int | None = get_first_element(sample_list)
    if first_item is not None:
        print(f"First element: {first_item}")