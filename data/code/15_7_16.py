from typing import List, TypeVar

T = TypeVar('T')

def get_second_last(lst: List[T]) -> T:
    if len(lst) < 2:
        raise IndexError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_second_last(sample_list)
    print(result)