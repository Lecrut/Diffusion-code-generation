from typing import Any, List, Dict
def append_to_collection(collection: List[Any], item: Any) -> None:
    if not isinstance(collection, list):
        raise TypeError("The first argument must be a list.")
    collection.append(item)
if __name__ == '__main__':
    initial_data: List[Any] = [42, "simple_string", {"nested": True}]
    append_to_collection(initial_data, 3.14)
    complex_dict: Dict[str, Any] = {
        "outer_key": [10, 20],
        "inner_value": {"deeply_nested": False}
    }
    append_to_collection(initial_data, complex_dict)
    print("Final Collection:", initial_data)