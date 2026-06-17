from typing import List, Any, Optional
def safe_read(data: List[Any], index: int, default: Any) -> Any:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    return data[index] if 0 <= index < len(data) else default
def update_slot(data: List[Any], index: int, value: Any) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if not (0 <= index < len(data)):
        raise IndexError(f"Index {index} out of range for list of length {len(data)}")
    data[index] = value
def validate_integrity(data: List[Any]) -> bool:
    return isinstance(data, list) and all(isinstance(item, type(None)) or not isinstance(item, (list, dict)) for item in data)
if __name__ == '__main__':
    sample_data: List[int] = [10, 20, 30, 40, 50]
    result_read = safe_read(sample_data, -1, "MISSING")
    update_slot(sample_data, len(sample_data) // 2, 99)
    is_valid = validate_integrity(sample_data)
    print(f"Read value: {result_read}")
    print(f"Updated data: {sample_data}")
    print(f"Integrity valid: {is_valid}")