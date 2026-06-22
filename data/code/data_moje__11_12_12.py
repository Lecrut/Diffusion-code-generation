from typing import Any, List

def get_last_item(items: List[Any]) -> Any:
    if not items:
        raise IndexError("Cannot get the last item of an empty list.")
    return items[len(items) - 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)