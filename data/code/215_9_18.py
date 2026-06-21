from typing import List

def find_maximum(data: List[int]) -> int:
    if not data:
        raise ValueError("Input list cannot be empty")
    max_value = data[0]
    for value in data[1:]:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    result = find_maximum(sample_list)
    print(f"The maximum element in {sample_list} is: {result}")