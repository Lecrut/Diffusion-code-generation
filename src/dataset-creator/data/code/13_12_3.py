from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def find_max_value(iterable: Iterable[Union[int, float]]) -> Union[int, float]:
    try:
        iterator = iter(iterable)
        max_value = next(iterator)
        for item in iterator:
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                if item > max_value:
                    max_value = item
            else:
                raise TypeError(f"Expected numeric type, got {type(item).__name__}")
    except StopIteration:
        raise ValueError("The provided sequence is empty.") from None
    return max_value
if __name__ == '__main__':
    sample_data_1 = [3.5, 7, -2, 9.8]
    sample_data_2 = []
    print(f"Max of {sample_data_1}:")
    try:
        result = find_max_value(sample_data_1)
        print(result)
    except ValueError as ve:
        print(ve)
    print("\nMax of empty list:")
    try:
        result = find_max_value(sample_data_2)
        print(result)
    except (ValueError, TypeError) as e:
        print(f"Error occurred: {e}")