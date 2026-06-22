from typing import Any, List, TypeVar

T = TypeVar('T')

def get_second_last_element(items: List[T]) -> T:
    if len(items) < 2:
        raise ValueError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_second_last_element(sample_data)
    print(result)