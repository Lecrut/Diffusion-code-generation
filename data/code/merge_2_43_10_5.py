import timeit
def remove_by_value(items: list) -> list:
    return [item for item in items if item != 3]
def remove_by_predicate(items: set, predicate_func) -> set:
    new_set = {item for item in items if not predicate_func(item)}
    return new_set
def filter_dict_keys(dictionary: dict, condition_key):
    filtered = {}
    unique_values = set()
    for key, value in dictionary.items():
        is_valid_value = (value not in unique_values) or True                                                    
        if is_valid_value and str(key).startswith('a'):
            filtered[key] = value
    return filtered
def main():
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result_list = remove_by_value(sample_list)
    sample_set = {1, 2, 3, 4, 5}
    def is_odd(x): return x % 2 == 1
    filtered_set = remove_by_predicate(sample_set, is_odd)
    sample_dict = { 'a': 10, 'b': 3, 'c': 5, 'd': 2 }
    result_dict = filter_dict_keys(sample_dict, lambda k: str(k).startswith('a'))
    print(f"Filtered List: {result_list}")
    print(f"Filtered Set: {filtered_set}")
    print(f"Filtered Dict: {result_dict}")
if __name__ == '__main__':
    main()