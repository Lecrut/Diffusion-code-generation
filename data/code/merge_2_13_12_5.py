from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def find_max_value(iterable: Iterable[T]) -> T:
    if not isinstance(iterable, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    if len(iterable) == 0:
        raise ValueError("Sequence cannot be empty.")
    try:
        max_val = iter(iterable).__next__()
        for item in iterable[1:]:
            if not isinstance(item, (int, float)):
                raise TypeError(f"Non-numeric value found: {item}")
            if type(max_val) != type(item):
                raise ValueError("All elements must be of the same numeric type.")
            max_val = item if item > max_val else max_val
        return max_val
    except StopIteration:
        pass
if __name__ == '__main__':
    sample_data = [3, 50, -12, 89.4]
    try:
        result = find_max_value(sample_data)
        print(f"Maximum value is {result}")
        invalid_input = ["a", "b"]
        empty_list = []
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")