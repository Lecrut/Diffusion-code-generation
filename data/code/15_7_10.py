from typing import List, TypeVar

T = TypeVar('T')

def get_second_last(lst: List[T]) -> T:
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_second_last(sample_list)
    print(result)