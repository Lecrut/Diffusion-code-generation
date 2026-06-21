from typing import TypeVar, List

T = TypeVar('T')

def get_last_item(data: List[T]) -> T:
    index = len(data) - 1
    return data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)