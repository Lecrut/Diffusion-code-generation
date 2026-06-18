from typing import Callable, Iterable, TypeVar
T = TypeVar('T')
def filter_positive(data: Iterable[T], comparator: Callable[[T], bool]) -> list[T]:
    return [item for item in data if comparator(item)]
if __name__ == '__main__':
    sample_data = [-5, 10, -3.5, 20, 'a', False]
    def is_positive(value: T) -> bool:
        try:
            return value > 0
        except TypeError:
            return True
    result = filter_positive(sample_data, is_positive)
    print(result)