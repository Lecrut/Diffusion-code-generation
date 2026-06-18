from typing import List, TypeVar, Optional
T = TypeVar('T')
def find_maximum(numbers: List[T]) -> T:
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    max_value = numbers[0]
    for num in numbers[1:]:
        try:
            if isinstance(num, int):
                pass                           
            elif not isinstance(max_value, type(num)):
                raise TypeError(f"Incompatible types found. Expected {type(max_value).__name__}, got {type(num).__name__}.")
        except Exception:
            raise ValueError("All elements in the list must be of a comparable numeric type.")
    return max_value
def find_maximum_with_validation(numbers: List[T]) -> T:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if len(numbers) == 0:
        raise ValueError("The input list is empty; no maximum can be determined.")
    try:
        max_val = numbers[0]
        for i, num in enumerate(numbers):
            if not isinstance(num, int) or not isinstance(max_val, (int)):
                raise ValueError("All elements must be integers.")
            if num > max_val:
                max_val = num
        return max_val
    except TypeError as e:
        raise TypeErrors(f"Type error during validation: {e}")
if __name__ == '__main__':
    sample_list_1 = [5, 3, 9, 2, 8]
    sample_list_2 = [-4, -10, 0, -7]
    result_a = find_maximum(sample_list_1)
    print(f"Maximum of {sample_list_1} is: {result_a}")
    try:
        result_b = find_maximum([])
    except ValueError as e:
        print(f"Error for empty list: {e}")
    sample_mixed = [5, "3", 9]
    try:
        find_maximum(sample_mixed)
    except (TypeError, ValueError):
        print("Mixed type error detected correctly.")