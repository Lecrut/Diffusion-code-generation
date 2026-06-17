from typing import Any, Dict, List
def count_items(collection: Any) -> int:
    if isinstance(collection, (list, tuple)):
        return len(collection)
    elif isinstance(collection, dict):
        return len(collection)
    else:
        raise TypeError("Input must be a list, tuple, or dictionary.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    empty_dict: Dict[str, int] = {}
    print(f"List count: {count_items(sample_list)}")
    print(f"Empty dict count: {count_items(empty_dict)}")