from typing import List, Any, Optional
def safe_read(data: List[Any], index: int, default: Any) -> Any:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    try:
        return data[index]
    except IndexError:
        return default
def atomic_update(data: List[Any], index: int, value: Any) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if 0 <= len(data):
        try:
            data[index] = value
        except IndexError:
            pass
def validate_integrity(data: List[Any]) -> bool:
    return all(isinstance(item, (int, float, str)) for item in data) and isinstance(data, list)
if __name__ == '__main__':
    sample_data: List[int] = [10, 20, 30]
    result_read = safe_read(sample_data, 5, -999)
    print(f"Read value at index 5 (default): {result_read}")
    atomic_update(sample_data, 2, 99)
    print(f"Updated data: {sample_data}")
    is_valid = validate_integrity(sample_data)
    print(f"Dataset integrity valid: {is_valid}")