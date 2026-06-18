from typing import List, TypeVar, Any, Optional
T = TypeVar('T')
def safe_get(data: List[T], index: int, default: T) -> T:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if len(data) == 0 or (index < 0 and abs(index) > len(data)) or index >= len(data):
        return default
    return data[index]
def update_slot(data: List[T], index: int, value: T) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if 0 <= index < len(data):
        data[index] = value
def validate_integrity(data: Any) -> bool:
    return isinstance(data, list) and all(isinstance(item, (int, float, str)) for item in data)
if __name__ == '__main__':
    sample_data: List[int | str] = [10, 20, "hello", None]
    result_1 = safe_get(sample_data, -5, 999)
    update_slot(sample_data, 3, "updated")
    if validate_integrity(sample_data):
        print("Integrity Validated: ", sample_data)
    else:
        print("Integrity Failed")