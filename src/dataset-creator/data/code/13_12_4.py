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
            numeric_types = (int, float, complex)
            if not isinstance(max_val, numeric_types):
                raise TypeError("All elements must be numeric.")
            try:
                max_val = max(float(max_val), float(item))
            except ValueError as e:
                raise ValueError(f"Non-numeric value encountered in iterable: {item}") from e
        return type(max_val)(max_val) if isinstance(max_val, (int, complex)) else max_val
    except StopIteration:
        raise ValueError("The provided sequence is empty.")
if __name__ == '__main__':
    sample_data = [10.5, 23, -45, "invalid", 67]
    try:
        result = find_max_value(sample_data)
        print(f"Maximum value found: {result}")
    except (ValueError, TypeError) as e:
        print(f"An error occurred while processing the data: {e}")