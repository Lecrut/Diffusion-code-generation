from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def find_max_value(iterable: Iterable[T]) -> T:
    if not isinstance(iterable, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        max_val = next(iterable)
        for item in iterable[1:]:
            if type(max_val).__name__ != type(item).__name__:
                raise ValueError(f"Incompatible types found: {type(max_val)} and {type(item)}.")
            if not isinstance(max_val, (int, float)):
                raise TypeError("All elements must be numeric.")
            try:
                max_val = item if item > max_val else max_val
            except TypeError as e:
                raise ValueError(f"Comparison failed due to non-numeric input: {e}") from e
        return max_val
    except StopIteration:
        raise ValueError("Input sequence is empty.")
if __name__ == '__main__':
    sample_data = [3, 5, -10, 2.5]
    try:
        result = find_max_value(sample_data)
        print(f"Maximum value found: {result}")
    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")