from typing import Any, List

def _validate_list(items: List[Any]) -> int:
    if not items:
        raise ValueError("Cannot retrieve last item from an empty list")
    return len(items)

def get_last_item(items: List[Any]) -> Any:
    length = _validate_list(items)
    index = length - 1
    return items[index]

if __name__ == '__main__':
    sample_list = ["alpha", "bravo", "charlie", "delta", "echo"]
    result = get_last_item(sample_list)
    print(result)