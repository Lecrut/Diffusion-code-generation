from typing import List, Dict, Any
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
def process_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for item in data:
        key = item.get("name", "Unknown")
        value = item.get("value", 0)
        result[key] = value
    return result
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 5]
    sample_data = [
        {"name": "Alice", "value": 100},
        {"name": "Bob", "value": 250},
        {"name": "Charlie", "value": 150}
    ]
    sum_result = calculate_sum(sample_numbers)
    print(f"Sum of sample numbers: {sum_result}")
    max_result = find_max(sample_numbers)
    print(f"Maximum of sample numbers: {max_result}")
    processed_data = process_data(sample_data)
    print("Processed data:")
    for key, value in processed_data.items():
        print(f"{key}: {value}")