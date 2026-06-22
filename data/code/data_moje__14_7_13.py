from typing import Sequence, TypeVar

T = TypeVar('T')

def get_third_item(items: Sequence[T]) -> T:
    if len(items) < 3:
        raise IndexError("List must contain at least three items")
    return items[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third_item(sample_list)
    print(result)