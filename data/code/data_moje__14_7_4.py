from typing import Any, List

def get_third_item(items: List[Any]) -> Any:
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    if len(items) < 3:
        raise IndexError("List must contain at least three items to retrieve the third one.")
    return items[2]

if __name__ == "__main__":
    sample_data = ["apple", "banana", "cherry", "date", "elderberry"]
    result = get_third_item(sample_data)
    print(result)