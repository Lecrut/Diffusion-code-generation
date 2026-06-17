import time
def remove_from_list(items: list, criteria) -> tuple[list]:
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    filtered = [item for item in items if not criteria(item)]
    return filtered
def remove_from_set(items: set, criteria) -> tuple[set]:
    if not isinstance(items, set):
        raise TypeError("Input must be a set.")
    removed = []
    new_items = {}                                                                               
    for item in list(items):
        if not criteria(item):
            items.discard(item)
            removed.append(item)
    return items, set(removed)
def remove_from_dict(data: dict, key_criteria) -> tuple[dict]:
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary.")
    removed_keys = []
    new_data = {}
    for k in list(data.keys()):
        if key_criteria(k):
            del data[k]
            removed_keys.append(k)
    return data, set(removed_keys)
def main():
    sample_list = [10, 20, 30, 'a', 'b']
    def is_even(item):
        if isinstance(item, int):
            return item % 2 == 0
        return False
    filtered_list = remove_from_list(sample_list.copy(), is_even)
    sample_set = {1, 2, 3, 4}
    removed_items, _ = remove_from_set(sample_set.copy(), lambda x: x > 2.5)
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    def is_odd_key(key):
        return key in ['a', 'c']
    filtered_dict, removed_keys = remove_from_dict(sample_dict.copy(), is_odd_key)
if __name__ == '__main__':
    main()