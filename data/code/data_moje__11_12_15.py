from typing import TypeVar, List

T = TypeVar('T')

INDEX_OFFSET: int = 1

def get_last_element(data: List[T]) -> T:
    if not data:
        raise IndexError("Cannot retrieve the last element from an empty list")
    target_index: int = len(data) - INDEX_OFFSET
    return data[target_index]

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    final_item = get_last_element(sample_data)
    print(final_item)