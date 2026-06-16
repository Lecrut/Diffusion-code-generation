from typing import List, TypeVar, Union
T = TypeVar('T')
def find_maximum(numbers: List[Union[int, float]]) -> Union[int, float]:
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
    test_cases = [
        [-5, -2, 10, 3],
        [3.5, 7.2, 4.8, 9.1],
        [10]
    ]
    for i, data in enumerate(test_cases):
        try:
            result = find_maximum(data)
            print(f"Test case {i + 1}: Maximum value is {result}")
        except Exception as e:
            print(f"Error in test case {i + 1}: {e}")