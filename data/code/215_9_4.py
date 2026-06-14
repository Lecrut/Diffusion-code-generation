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
    sample_list_int = [10, 4, 25, 8, 30]
    print(f"List: {sample_list_int}")
    max_int = find_maximum(sample_list_int)
    print(f"Maximum element in {sample_list_int}: {max_int}")
    sample_list_float = [3.14, 1.618, 2.718]
    print(f"\nList: {sample_list_float}")
    max_float = find_maximum(sample_list_float)
    print(f"Maximum element in {sample_list_float}: {max_float}")
    sample_list_empty: List[int] = []
    try:
        find_maximum(sample_list_empty)
    except ValueError as e:
        print(f"\nError handling for empty list: {e}")