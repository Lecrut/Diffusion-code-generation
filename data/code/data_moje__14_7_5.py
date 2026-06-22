from typing import Sequence, TypeVar

T = TypeVar('T')

def get_third_item(lst: Sequence[T]) -> T:
    if len(lst) < 3:
        raise IndexError("List must contain at least three items.")
    return lst[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_third_item(sample_list)
    print(result)