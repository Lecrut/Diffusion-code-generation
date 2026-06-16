from typing import Any, Collection, Set
def is_contained(obj: Any, collection: Collection[Any]) -> bool:
    try:
        return obj in collection
    except TypeError:
        for item in collection:
            if isinstance(item, type(obj)) and (item == obj):
                return True
        return False
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_set = {40, 50}
    target_value = 20
    result_list = is_contained(target_value, sample_list)
    result_set = is_contained(60, sample_set)
    print(f"Value in list: {result_list}")
    print(f"Value in set: {result_set}")