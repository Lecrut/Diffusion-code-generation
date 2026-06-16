from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def find_max(iterable: Iterable[Union[int, float]]) -> Union[int, float]:
    iterator = iter(iterable)
    try:
        max_val = next(iterator)
        for item in iterator:
            if not isinstance(item, (int, float)):
                raise TypeError(f"Expected numeric value, got {type(item).__name__}")
            if item > max_val:
                max_val = item
        return max_val
    except StopIteration:
        raise ValueError("The sequence is empty.")
if __name__ == '__main__':
    sample_data = [3.5, 7, -10, 20.8, 'invalid', None]
    try:
        result = find_max(sample_data)
        print(f"Maximum value found: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")