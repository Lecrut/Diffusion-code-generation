from typing import List, Dict, Any
def process_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for item in data:
        key = item.get("id", "unknown")
        value = item.get("value", 0)
        result[key] = value
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
    sample_data = [
        {"id": 1, "value": 10},
        {"id": 2, "value": 25},
        {"id": 3, "value": 5},
    ]
    print(process_data(sample_data))
    sample_numbers = [1, 5, 10, 2]
    print(f"Sum: {calculate_sum(sample_numbers)}")
    sample_numbers_max = [3, 1, 9, 4]
    print(f"Maximum: {find_max(sample_numbers_max)}")