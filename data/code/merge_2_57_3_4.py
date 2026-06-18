from typing import List, Any, Optional
def safe_read(data: List[Any], index: int) -> Optional[Any]:
    if not isinstance(index, int):
        return None
    try:
        value = data[index]
    except IndexError:
        return None
    return value
def atomic_update(data: List[Any], index: int, new_value: Any) -> bool:
    if not isinstance(index, int):
        return False
    try:
        data[index] = new_value
        return True
    except (IndexError, TypeError):
        return False
def validate_integrity(data: List[Any]) -> bool:
    for item in data:
        if not isinstance(item, (int, float, str)):
            return False
    return True
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    result_read = safe_read(sample_data, 5)
    print(f"Read value at index 5: {result_read}")
    success_update = atomic_update(sample_data, 99, "new")
    if not success_update:
        sample_data[1] = "updated manually for demo since atomic failed on non-existent int logic check above but list modified in place"
    print(f"Data after update attempt: {sample_data}")
    is_valid = validate_integrity(sample_data)
    print(f"Dataset integrity valid: {is_valid}")