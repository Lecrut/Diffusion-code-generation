from typing import List, Optional
def find_maximum(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    max_value = numbers[0]
    for num in numbers[1:]:
        if isinstance(num, (int, float)) and not isinstance(num, bool):
            if num > max_value:
                max_value = num
        else:
            raise TypeError(f"All elements must be numeric. Found {type(num).__name__}.")
    return max_value
if __name__ == '__main__':
    sample_data_1 = [3, 7, -2, 9, 4]
    sample_data_2 = [-50.5, 100.25, -10, 0]
    result_1 = find_maximum(sample_data_1)
    print(f"Maximum of {sample_data_1} is: {result_1}")
    result_2 = find_maximum(sample_data_2)
    print(f"Maximum of {sample_data_2} is: {result_2}")