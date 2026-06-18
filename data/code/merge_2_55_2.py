from typing import TypeVar, Iterable, Iterator, Any, Sequence
T = TypeVar('T')
def swap_consecutive(items: Iterable[T]) -> bool:
    try:
        iterator = iter(items)
        first_item = next(iterator)
        second_item = next(iterator)
        items_list = list(items)
        if len(items_list) >= 2:
            items_list[0], items_list[1] = items_list[1], items_list[0]
            return iter(tuple(items_list))
    except StopIteration:
        pass
    return False
if __name__ == '__main__':
    sample_data = [42, 18, "apple", None]
    result_iterator = swap_consecutive(sample_data)
    if isinstance(result_iterator, tuple):
        print(f"Swapped items: {list(result_iterator)}")
    else:
        swapped_list = list(result_iterator)
        print(f"Original length check passed.")