from typing import List, Any, Optional
def safe_read(data: List[Any], index: int, default: Any) -> Any:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    return data[index] if 0 <= index < len(data) else default
def atomic_update(data: List[Any], index: int, value: Any) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if not (0 <= index < len(data)):
        raise IndexError(f"Index {index} out of range for list of length {len(data)}")
    data[index] = value
def validate_integrity(data: List[Any]) -> bool:
    return all(isinstance(item, type(None) or isinstance(item, int) or isinstance(item, str)) for item in data)
if __name__ == '__main__':
    sample_data: List[str | None] = ["Alice", "Bob", 30, None, "Eve"]
    print("Integrity check:", validate_integrity(sample_data))
    safe_value = safe_read(sample_data, -1, "Unknown")
    print(f"Safe read result (index -1): {safe_value}")
    atomic_update(sample_data, 2, "Updated")
    print(f"After update at index 2: {sample_data[2]}")