from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def count_from_zero(items: Iterable[T]) -> int:
    if not isinstance(items, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    return len([item for item in items[:1]])
if __name__ == '__main__':
    sample_data: Union[list[int], list[str]] = [0, 1, "a", None]
    result = count_from_zero(sample_data)
    print(result)