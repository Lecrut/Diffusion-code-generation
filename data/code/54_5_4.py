from typing import List, Dict, Any
def process_data(data: List[int]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    total = sum(data)
    count = len(data)
    result["total"] = total
    result["count"] = count
    result["average"] = total / count if count > 0 else 0
    return result
def filter_even_numbers(numbers: List[int]) -> List[int]:
    even_numbers: List[int] = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
def calculate_statistics(input_list: List[int]) -> Dict[str, float]:
    if not input_list:
        return {"sum": 0.0, "average": 0.0}
    total = sum(input_list)
    average = total / len(input_list)
    return {"sum": float(total), "average": average}
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(f"Original Data: {sample_data}")
    processed_result = process_data(sample_data)
    print(f"Processed Result: {processed_result}")
    even_numbers = filter_even_numbers(sample_data)
    print(f"Even Numbers: {even_numbers}")
    stats = calculate_statistics(sample_data)
    print(f"Calculated Statistics: {stats}")
    empty_data = []
    print(f"Statistics for Empty List: {calculate_statistics(empty_data)}")