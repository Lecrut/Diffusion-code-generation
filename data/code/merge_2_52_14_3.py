from typing import TypeVar, Iterable, Any
T = TypeVar('T')
def get_last_item(sequence: Iterable[T]) -> T | None:
    try:
        return next(reversed(sequence))
    except StopIteration:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_item(sample_list)
    print(result)