import functools
from typing import Any, Callable, Dict, Iterable, List, Set, Tuple
class FilterUtils:
    @staticmethod
    def filter_by_value(
        collection: Iterable[Any], predicate: Callable[[Any], bool]
    ) -> List[Any]:
        if not isinstance(collection, (list, tuple)):
            raise TypeError(f"Input must be a list or tuple, got {type(collection)}")
        if not callable(predicate):
            raise TypeError("Predicate function must be callable")
        return [item for item in collection if predicate(item)]
    @staticmethod
    def filter_by_key(
        data: Dict[Any, Any], key_predicate: Callable[[Any], bool]
    ) -> List[Tuple[Any, Any]]:
        if not isinstance(data, dict):
            raise TypeError(f"Input must be a dictionary, got {type(data)}")
        if not callable(key_predicate):
            raise TypeError("Key predicate function must be callable")
        return [(k, v) for k, v in data.items() if key_predicate(k)]
    @staticmethod
    def remove_duplicates_from_list(items: List[Any]) -> Set[Any]:
        if not isinstance(items, list):
            raise TypeError(f"Input must be a list, got {type(items)}")
        return set(items)
    @staticmethod
    def filter_set_by_condition(
        data: Set[Any], condition_fn: Callable[[Any], bool]
    ) -> List[Any]:
        if not isinstance(data, set):
            raise TypeError(f"Input must be a set, got {type(data)}")
        if not callable(condition_fn):
            raise TypeError("Condition function must be callable")
        return [item for item in data if condition_fn(item)]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b', None]
    def is_even(n):
        return isinstance(n, int) and n % 2 == 0
    removed_items = FilterUtils.filter_by_value(sample_list, lambda x: not (x in [1, 3]))
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    def is_odd_key(k):
        return isinstance(k, str) and int(k[0]) % 2 != 0
    filtered_keys_values = FilterUtils.filter_by_key(sample_dict, lambda k: not (k in ['a', 'b']))
    sample_tuple = ('x', 'y', 'z')
    def starts_with_x(item):
        return isinstance(item, str) and item.startswith('x')
    filtered_tuple_items = FilterUtils.filter_by_value(sample_tuple, lambda i: not (i == 'x'))
    sample_set = {10, 20, 30}
    def is_greater_than_5(val):
        return isinstance(val, int) and val > 5
    filtered_set_items = FilterUtils.filter_set_by_condition(sample_set, lambda v: not (v == 10))
    print(f"Removed from list: {removed_items}")
    print(f"Filtered dict entries: {filtered_keys_values}")
    sample_list_with_dups = [5, 2, 8, 3, 'a', 'b']
    deduplicated_set = FilterUtils.remove_duplicates_from_list(sample_list_with_dups)
    print(f"Deduplicated set: {deduplicated_set}")