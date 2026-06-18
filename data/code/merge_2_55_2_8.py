from typing import TypeVar, Iterable, Iterator
T = TypeVar('T')
def swap_consecutive(iterable: Iterable[T]) -> list[T]:
    try:
        iterator = iter(iterable)
        first_item = next(iterator)
        second_item = next(iterator)
        swapped_list = [first_item, second_item]
        for item in iterator:
            if len(swapped_list) == 2:
                swapped_list.append(second_item)
                swapped_list.insert(1, first_item)
            else:
                swapped_list.append(item)
    except StopIteration:
        return list(iterable)
    return swapped_list
if __name__ == '__main__':
    sample_data = [42, 3.14, "hello", None]
    result = swap_consecutive(sample_data)
    print(result)