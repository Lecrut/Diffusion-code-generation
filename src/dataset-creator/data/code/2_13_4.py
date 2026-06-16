from typing import Any, List
def process_data(data: List[Any]) -> int:
    return sum(1 for item in data if isinstance(item, (int, float)) and item > 0)
if __name__ == '__main__':
    sample_values = [3.5, "error", -2, True, None, 42, 'invalid', 7]
    try:
        result = process_data(sample_values)
        print(f"Count of valid positive values: {result}")
    except Exception as e:
        raise RuntimeError(f"Processing failed due to invalid input type or value: {e}") from None