from typing import List, Dict, Any
def process_data(data: List[int]) -> List[int]:
    result: List[int] = []
    for item in data:
        result.append(item * 2)
    return result
def calculate_sum(numbers: List[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total
def find_max(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_val = numbers[0]
    for number in numbers[1:]:
        if number > max_val:
            max_val = number
    return max_val
if __name__ == '__main__':
    sample_list_one = [1, 2, 3, 4, 5]
    sample_list_two = [10, 20, 30]
    processed_list = process_data(sample_list_one)
    print(f"Processed list: {processed_list}")
    sum_result = calculate_sum(sample_list_two)
    print(f"Sum of sample two: {sum_result}")
    max_result = find_max(sample_list_one)
    print(f"Maximum of sample one: {max_result}")