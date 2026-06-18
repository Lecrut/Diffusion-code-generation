from typing import List, Any
def process_positive_values(data: List[Any]) -> int:
    return sum(1 for item in data if isinstance(item, (int, float)) and item > 0)
if __name__ == '__main__':
    sample_data = [3.5, "invalid", -2, None, True, 4, [], {}, "error"]
    try:
        count = process_positive_values(sample_data)
        print(f"Count of positive values: {count}")
    except Exception as e:
        raise TypeError("Invalid input detected in data list.") from e