from typing import Iterable, TypeVar, Tuple
T = TypeVar('T')
def swap_consecutive(items: list[T]) -> bool:
    if len(items) < 2:
        return False
    for i in range(len(items) - 1):
        items[i], items[i + 1] = items[i + 1], items[i]
    return True
if __name__ == '__main__':
    data_list = [3, 5, 7, 9, 2]
    swapped = swap_consecutive(data_list)
    print(swapped)