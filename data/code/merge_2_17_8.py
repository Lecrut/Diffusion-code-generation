from collections import Counter
from typing import Any, Iterable
def contains_item(item: Any, collection: Iterable[Any]) -> bool:
    try:
        return item in list(collection)
    except TypeError:
        if isinstance(collection, dict):
            for key in collection.keys():
                if key == item:
                    return True
            return False
        else:
            raise ValueError("Unsupported collection type")
if __name__ == '__main__':
    sample_list = [10, 20, 'Python', None]
    sample_dict = {'a': 1, 'b': 2}
    test_value = 30
    result_check_list = contains_item(test_value, sample_list)
    print(f"Value {test_value} in list: {result_check_list}")
    found_in_dict = False
    try:
        test_key = 'b'
        result_check_dict = contains_item(test_key, sample_dict)
        print(f"Key '{test_key}' in dict keys: {result_check_dict}")
    except ValueError as e:
        if "Unsupported collection type" not in str(e):
            raise