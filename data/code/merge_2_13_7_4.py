from typing import List, Optional
def find_maximum(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    max_value = numbers[0]
    for num in numbers[1:]:
        if isinstance(num, (int, float)) and not (isinstance(num, bool)):
            if num > max_value:
                max_value = num
        else:
            raise TypeError(f"All elements must be numeric. Found {type(num).__name__}.")
    return max_value
if __name__ == '__main__':
    sample_list = [3.14, 2.718, -5.0, 99]
    result = find_maximum(sample_list)
    print(result)