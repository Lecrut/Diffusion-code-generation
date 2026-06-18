from typing import Any, Callable, Dict, List, Set, Tuple
class FilterError(Exception):
    pass
def filter_by_condition(
    data: Any, 
    condition: Callable[[Any], bool]
) -> Any:
    try:
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if not condition(k)}
        elif isinstance(data, list):
            result = []
            for item in data:
                try:
                    should_remove = condition(item)
                    if not should_remove:
                        result.append(item)
                except Exception as e:
                    raise FilterError(f"Condition failed during evaluation of {item}: {e}") from e
            return result
        elif isinstance(data, set):
            filtered_set = set()
            for item in data:
                try:
                    should_remove = condition(item)
                    if not should_remove:
                        filtered_set.add(item)
                except Exception as e:
                    raise FilterError(f"Condition failed during evaluation of {item}: {e}") from e
            return filtered_set
        elif isinstance(data, tuple):
            result_tuple = ()
            for item in data:
                try:
                    should_remove = condition(item)
                    if not should_remove:
                        result_tuple += (item,)
                except Exception as e:
                    raise FilterError(f"Condition failed during evaluation of {item}: {e}") from e
            return result_tuple
        else:
            raise FilterError("Unsupported data type. Only List, Set, Tuple, and Dict are supported.")
    except Exception as e:
        raise
def filter_by_value_condition(
    data: Any, 
    condition: Callable[[Any], bool]
) -> Any:
    try:
        if isinstance(data, list):
            result = []
            for item in data:
                try:
                    should_remove = condition(item)
                    if not should_remove:
                        result.append(item)
                except Exception as e:
                    raise FilterError(f"Condition failed during evaluation of {item}: {e}") from e
            return result
        elif isinstance(data, set):
            filtered_set = set()
            for item in data:
                try:
                    should_remove = condition(item)
                    if not should_remove:
                        filtered_set.add(item)
                except Exception as e:
                    raise FilterError(f"Condition failed during evaluation of {item}: {e}") from e
            return filtered_set
        elif isinstance(data, tuple):
            result_tuple = ()
            for item in data:
                try:
                    should_remove = condition(item)
                    if not should_remove:
                        result_tuple += (item,)
                except Exception as e:
                    raise FilterError(f"Condition failed during evaluation of {item}: {e}") from e
            return result_tuple
        else:
            raise FilterError("Value condition not supported for Dictionary type in this variant.")
    except Exception as e:
        raise
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    def remove_multiples_of_5(x): return x % 5 == 0
    filtered_result = filter_by_condition(sample_list, remove_multiples_of_5)
    print("Original List:", sample_list)
    print("Filtered Result (removed multiples of 5):", filtered_result)
    sample_set = {10, 20, 30, 40}
    set_filtered = filter_by_condition(sample_set, remove_multiples_of_5)
    print("\nOriginal Set:", sample_set)
    print("Filtered Result (removed multiples of 5):", set_filtered)
    sample_tuple: tuple[int] = (10, 20, 30)
    tuple_filtered = filter_by_condition(sample_tuple, remove_multiples_of_5)
    print("\nOriginal Tuple:", sample_tuple)
    print("Filtered Result (removed multiples of 5):", tuple_filtered)
    def check_even_key_val(x: int) -> bool: return x % 2 == 0
    sample_dict = {'a': 1, 'b': 4, 'c': 7}
    def remove_key_a(key: str) -> bool: return key == 'a'
    dict_filtered = filter_by_condition(sample_dict, remove_key_a)
    print("\nOriginal Dict:", sample_dict)
    print("Filtered Result (removed key 'a'):")
    for k, v in dict_filtered.items(): 
        pass
    print(dict_filtered)
    try:
        filter_by_condition("not a list", remove_multiples_of_5)
    except FilterError as e:
        print(f"\nCaught expected error for unsupported type: {e}")