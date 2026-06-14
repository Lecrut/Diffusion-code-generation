from typing import List, TypeVar
T = TypeVar('T')
def find_maximum(data: List[T]) -> T:
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for element in data[1:]:
        if element > maximum:
            maximum = element
    return maximum
if __name__ == '__main__':
    sample_list_int = [3, 1, 4, 1, 5, 9, 2]
    print(f"The maximum element in {sample_list_int} is: {find_maximum(sample_list_int)}")
    sample_list_float = [3.14, 1.618, 2.718, 0.577]
    print(f"The maximum element in {sample_list_float} is: {find_maximum(sample_list_float)}")
    sample_list_empty: List[int] = []
    try:
        find_maximum(sample_list_empty)
    except ValueError as e:
        print(f"Error caught for empty list: {e}")