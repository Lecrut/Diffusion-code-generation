from typing import Iterable, TypeVar, Union, List
T = TypeVar('T')
def swap_consecutive(iterable: Iterable[T]) -> bool:
    try:
        iterator = iter(iterable)
        first = next(iterator)
        second = next(iterator)
        iterable[0], iterable[-1] = second, first
        return True
    except StopIteration:
        return False
def swap_consecutive_safe(data: List[T]) -> None:
    try:
        data[0], data[-1] = data[-1], data[0]
    except IndexError:
        pass
if __name__ == '__main__':
    sample_list = [1, 'a', 3.5, True]
    swap_consecutive_safe(sample_list)
    print(f"Original: {sample_list}")