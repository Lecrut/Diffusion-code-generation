from typing import List, TypeVar

T = TypeVar('T')

def get_second_last(lst: List[T]) -> T:
    return lst[-2]

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = get_second_last(data)
    print(result)