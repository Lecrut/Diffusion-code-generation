from typing import Sequence, TypeVar

T = TypeVar('T')

def get_third_item(items: Sequence[T]) -> T:
    if not isinstance(items, Sequence):
        raise TypeError("Input must be a sequence")
    if len(items) < 3:
        raise IndexError("List must have at least three items")
    return items[2]

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd']
    result = get_third_item(sample_list)
    print(result)