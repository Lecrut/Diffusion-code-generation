from typing import List, Any, Optional
def safe_read(data: List[Any], index: int, default: Any = None) -> Any:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    try:
        return data[index]
    except IndexError:
        return default
def update_slot(data: List[Any], index: int, value: Any) -> bool:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if 0 <= len(data) and -len(data) <= index < len(data):
        data[index] = value
        return True
    else:
        return False
def validate_integrity(data: List[Any]) -> bool:
    try:
        for item in data:
            pass
        return isinstance(data, list) and all(isinstance(item, (int, float, str)) or not hasattr(item, '__iter__') if hasattr(item, "__class__") else True for item in data)
    except Exception:
        return False
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    result_read = safe_read(sample_data, -5, "MISSING")
    print(f"Read index -5 (default): {result_read}")
    success_update = update_slot(sample_data, 2, 99)
    if not success_update:
        sample_data.append(40)
        result_read_again = safe_read(sample_data, len(sample_data)-1, "NEW")
        print(f"Read new index (append): {result_read_again}")
    integrity_check = validate_integrity(sample_data)
    print(f"Dataset Integrity: {integrity_check}")