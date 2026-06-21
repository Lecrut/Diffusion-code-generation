from typing import TypeVar, List

T = TypeVar("T")

def get_last_element(lst: List[T]) -> T:
    if not lst:
        raise ValueError("List must not be empty")
    return lst[-1]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    last = get_last_element(data)
    print(last)