from typing import Any, Callable, Dict, List, Set, TypeVar, Union
T = TypeVar('T')
def remove_by_condition(collection: Union[List[T], Set[T]], condition: Callable[[Any], bool]) -> None:
    if isinstance(collection, list):
        collection[:] = [item for item in collection if not condition(item)]
    elif isinstance(collection, set):
        collection.difference_update([item for item in collection if condition(item)])
def remove_by_key_in_dict(dictionary: Dict[Any, Any], keys_to_remove: List[Any]) -> None:
    to_delete = [key for key in dictionary.keys() if key in keys_to_remove]
    for key in to_delete:
        del dictionary[key]
def remove_by_value_in_dict(dictionary: Dict[Any, Any], values_to_remove: List[Any]) -> None:
    to_delete = [key for key, value in dictionary.items() if value in values_to_remove]
    for key in to_delete:
        del dictionary[key]
def remove_if_condition_in_dict(dictionary: Dict[Any, Any], condition: Callable[[Any], bool]) -> None:
    keys_to_delete = [key for key, value in dictionary.items() if condition(value)]
    for key in keys_to_delete:
        del dictionary[key]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'a', 'b', 'c']
    def is_even(x):
        return isinstance(x, int) and x % 2 == 0
    remove_by_condition(sample_list, is_even)
    sample_set = {5, 6, 7, 8}
    remove_by_condition(sample_set, lambda x: x > 6)
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    keys_to_remove_list = ['a', 'd']
    remove_by_key_in_dict(sample_dict, keys_to_remove_list)
    values_to_remove_list = [10, 20]
    sample_dict_with_values = {'x': 10, 'y': 30}
    remove_by_value_in_dict(sample_dict_with_values, values_to_remove_list)
    def is_odd(x):
        return isinstance(x, int) and x % 2 != 0
    remove_if_condition_in_dict({'p': 5, 'q': 10}, lambda v: v > 7)