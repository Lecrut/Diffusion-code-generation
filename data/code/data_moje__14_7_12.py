from typing import Any, List

def get_third_item(items: List[Any]) -> Any:
    if not isinstance(items, list):
        raise TypeError("Input must be a list")
    if len(items) < 3:
        raise IndexError("List does not contain a third item")
    return items[2]

if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print(get_third_item(sample_list))