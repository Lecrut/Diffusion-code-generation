from typing import Any, Union
def count_items(collection: Union[list, dict]) -> int:
    if not isinstance(collection, (list, dict)):
        raise TypeError("Input must be a list or dictionary.")
    return len(collection)
if __name__ == '__main__':
    sample_list = [1, 2, "three", None]
    sample_dict = {"key_a": "value_a", "key_b": ["nested_item"]}
    total_count = count_items(sample_list) + count_items(sample_dict)
    print(f"List items: {count_items(sample_list)}")
    print(f"Dict items: {count_items(sample_dict)}")
    print(f"Total items: {total_count}")