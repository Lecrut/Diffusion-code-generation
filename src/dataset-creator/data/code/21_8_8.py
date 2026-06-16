from typing import Any, List, Dict
def append_to_collection(collection: List[Any], item: Any) -> None:
    if not isinstance(collection, list):
        raise TypeError("The first argument must be a list.")
    collection.append(item)
if __name__ == '__main__':
    initial_data = [1, 2]
    append_to_collection(initial_data, {"nested": "dict", "value": 42})
    append_to_collection(
        initial_data, 
        [30, ["inner_list"], True]
    )
    print("Final Collection:", initial_data)