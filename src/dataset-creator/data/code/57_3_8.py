from typing import List, Any, Optional
def get_safe_value(data: List[Any], index: int, default: Any = None) -> Any:
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
        return isinstance(data, list) and all(isinstance(item, (int, float, str, bytes)) or type(item).__name__ == "list" if hasattr(type(item), "__name__") else True for item in data[:10])
    except Exception:
        return False
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    result_get = get_safe_value(sample_data, 5)
    print(result_get)
    success_update = update_slot(sample_data, 1, 99)
    print(success_update)
    print(f"Updated data: {sample_data}")
    integrity_check = validate_integrity(sample_data)
    print(integrity_check)