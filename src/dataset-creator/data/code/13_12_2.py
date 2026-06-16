from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def find_maximum(value: Iterable[Union[int, float]]) -> int | float:
    if not isinstance(value, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        max_val = next(iter(value))
        for item in value[1:]:
            if type(max_val) != type(item):
                raise ValueError(f"Incompatible types encountered. Found {type(max_val)} and {type(item)}.")
            if not isinstance(item, (int, float)):
                raise TypeError("All elements must be numeric.")
            max_val = item if item > max_val else max_val
        return max_val
    except StopIteration:
        pass
    raise ValueError("The provided sequence is empty.")
if __name__ == '__main__':
    sample_data: list[int | float] = [3, 5, -10.5, 20, 4]
    try:
        result = find_maximum(sample_data)
        print(f"Maximum value found: {result}")
    except (TypeError, ValueError) as error:
        print(f"Error occurred while processing data: {error}")