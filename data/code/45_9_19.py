from typing import List, Union

def get_minimum(numbers: List[Union[int, float]]) -> Union[int, float]:
    if not numbers:
        raise ValueError("List must not be empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = get_minimum(sample_values)
    print(result)