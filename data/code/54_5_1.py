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
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    sample_list_one = [1, 2, 3, 4, 5]
    sample_list_two = [10, 20, 30]
    sample_list_empty: List[int] = []
    processed_one = process_data(sample_list_one)
    print(f"Processed data for {sample_list_one}: {processed_one}")
    sum_two = calculate_sum(sample_list_two)
    print(f"Sum of data for {sample_list_two}: {sum_two}")
    max_one = find_max(sample_list_one)
    print(f"Maximum value in {sample_list_one}: {max_one}")
    try:
        find_max(sample_list_empty)
    except ValueError as e:
        print(f"Error caught for empty list: {e}")