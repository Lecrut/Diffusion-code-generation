from typing import List, TypeVar, Tuple, Union
T = TypeVar('T')
def find_maximum(values: List[T]) -> T:
    if not isinstance(values, list):
        raise TypeError("Input must be a list.")
    if len(values) == 0:
        raise ValueError("List is empty; cannot determine maximum.")
    try:
        first_value = values[0]
        max_val = first_value
        for item in values[1:]:
            if not isinstance(item, type(first_value)):
                raise TypeError(f"Type mismatch. Expected {type(first_value)}, got {type(item)}.")
            if item > max_val:
                max_val = item
        return max_val
    except Exception as e:
        raise RuntimeError("Error during maximum calculation.") from e
def find_maximum_optimized(values: List[T]) -> T:
    if not isinstance(values, list):
        raise TypeError("Input must be a list.")
    if len(values) == 0:
        raise ValueError("List is empty; cannot determine maximum.")
    try:
        return max(values)
    except Exception as e:
        raise RuntimeError("Error during maximum calculation.") from e
if __name__ == '__main__':
    sample_list = [3, 7, 2, 91, -4]
    result_standard = find_maximum(sample_list)
    result_optimized = find_maximum_optimized(sample_list)
    print(f"Standard Maximum: {result_standard}")
    print(f"Optimized Maximum: {result_optimized}")