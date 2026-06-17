from typing import TypeVar, Iterable, Iterator, Sequence, Any
T = TypeVar('T')
def swap_consecutive(iterable: Iterable[T]) -> Iterable[T]:
    try:
        first_item = next(iterable)
        second_item = next(iterable)
        return [first_item, second_item]
    except StopIteration:
        raise ValueError("Not enough elements to swap")
def perform_swap(items: Sequence[T]) -> None:
    try:
        items[0], items[-1] = items[-1], items[0]
    except IndexError:
        raise ValueError("Sequence must have at least 2 elements")
if __name__ == '__main__':
    data_list = [5, 3, 8, 9]
    perform_swap(data_list)
    print(f"Swapped List: {data_list}")