from typing import Iterable, TypeVar
T = TypeVar('T')
def get_first_element(iterable: Iterable[T]) -> T | None:
    try:
        return next(iter(iterable))
    except StopIteration:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_first_element(sample_list)
    print(result if result is not None else "No element found")