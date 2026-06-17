from typing import List, Any
def count_items_from_start(data: List[Any]) -> int:
    if not data:
        return 0
    target = data[0]
    count = sum(1 for item in data if isinstance(item, type(target)) and item == target)
    return count
if __name__ == '__main__':
    sample_data = [5, 5, "apple", 5, True, False, 5.0]
    result = count_items_from_start(sample_data)
    print(result)