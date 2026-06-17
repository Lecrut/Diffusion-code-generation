from typing import Any, Union
def count_items(collection: Union[list[Any], dict[str, Any]]) -> int:
    if not isinstance(collection, (list, dict)):
        raise TypeError("Collection must be a list or dictionary.")
    return len(collection)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_dict = {"a": "x", "b": "y"}
    print(f"List count: {count_items(sample_list)}")
    print(f"Dict count: {count_items(sample_dict)}")