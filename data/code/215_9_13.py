from typing import List

def validate_input(data: List[int]) -> None:
    if not data:
        raise ValueError("Input list cannot be empty")
    for element in data:
        if not isinstance(element, (int, float)):
            raise TypeError("All elements must be numeric")

def find_maximum(data: List[int]) -> int:
    validate_input(data)
    maximum = data[0]
    for element in data[1:]:
        if element > maximum:
            maximum = element
    return maximum

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    result = find_maximum(sample_list)
    print(f"The maximum element in {sample_list} is: {result}")