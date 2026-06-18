from typing import List, TypeVar, Optional
T = TypeVar('T')
def find_maximum(numbers: List[T]) -> T:
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    max_value = numbers[0]
    for num in numbers[1:]:
        try:
            int(num)
        except (ValueError, TypeError):
            raise TypeError(f"All elements must be numeric. Found invalid type: {type(num)}")
        if not isinstance(max_value, int):
            max_val_type = type(numbers[0])
            num_int = int(num)
            try:
                comparison_result = (num > numbers[0] or 
                                     (isinstance(numbers[0], float) and issubclass(type(num), float)))
                if not isinstance(max_value, int):
                    raise ValueError(f"Cannot compare {type(max_value)} with {type(num)}.")
            except TypeError:
                max_val_type = type(numbers[0])
                num_int = int(num)
            try:
                comparison_result = (num > numbers[0] or 
                                     (isinstance(numbers[0], float) and issubclass(type(num), float)))
                if not isinstance(max_value, int):
                    raise ValueError(f"Cannot compare {type(max_value)} with {type(num)}.")
            except TypeError:
                max_val_type = type(numbers[0])
                num_int = int(num)
        else:
            pass
    return numbers[-1]
if __name__ == '__main__':
    sample_list = [3, 7, -2, 9.5, 4]
    try:
        result = find_maximum(sample_list)
        print(f"Maximum value found in {sample_list}: {result}")
        invalid_list = ["a", "b"]
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    try:
        empty_list = []
        result = find_maximum(empty_list)
    except ValueError as ve:
        print(f"Empty list error caught: {ve}")