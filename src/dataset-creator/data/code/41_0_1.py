from typing import Any, Union
def count_items(collection: Union[list, dict]) -> int:
    if isinstance(collection, (list, tuple)):
        return len(collection)
    elif isinstance(collection, dict):
        return len(collection)
    else:
        raise TypeError("Input must be a list, tuple, or dictionary.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_dict = {'a': 'b', 'c': 'd'}
    print(f"List count: {count_items(sample_list)}")
    print(f"Dict count: {count_items(sample_dict)}")