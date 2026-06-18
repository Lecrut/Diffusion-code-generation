from typing import List, TypeVar
T = TypeVar('T')
def find_max_value(numbers: List[T]) -> T:
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    max_val = numbers[0]
    for item in numbers[1:]:
        try:
            if item > max_val:
                max_val = item
        except TypeError:
            raise TypeError(f"Cannot compare {type(item).__name__} with current maximum type.")
    return max_val
if __name__ == '__main__':
    sample_list_1: List[int] = [3, 7, 2, 9, 4]
    sample_list_2: List[float] = [-0.5, 0.0, 1.2, -2.8]
    result_int = find_max_value(sample_list_1)
    result_float = find_max_value(sample_list_2)
    print(f"Max of integers {sample_list_1}: {result_int}")
    print(f"Max of floats {sample_list_2}: {result_float}")