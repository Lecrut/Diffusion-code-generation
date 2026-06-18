from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def find_max_value(iterable: Iterable[T]) -> T:
    if not isinstance(iterable, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        max_val = next(iterable)
    except StopIteration:
        raise ValueError("The provided sequence is empty.") from None
    for item in iterable[1:]:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Expected numeric value, got {type(item).__name__}.")
        try:
            max_val = max(max_val, item)
        except ValueError as e:
            raise RuntimeError("Comparison failed due to non-numeric comparison.") from None
    return max_val
if __name__ == '__main__':
    sample_data: list[int] | tuple[float, ...] = [10.5, 23, -5, 44.67, 9]
    try:
        result = find_max_value(sample_data)
        print(f"Maximum value found: {result}")
    except (ValueError, TypeError) as exc:
        error_message = str(exc) if isinstance(exc, ValueError | TypeError) else "Unexpected error occurred."
        print(f"Error encountered: {error_message}")