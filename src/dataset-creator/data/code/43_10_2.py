import time
def remove_from_list(items: list, criteria) -> tuple[list]:
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    filtered = [item for item in items if not criteria(item)]
    return filtered
def remove_from_set(items: set, criteria) -> tuple[set]:
    if not isinstance(items, set):
        raise TypeError("Input must be a set.")
    result = {item for item in items if not criteria(item)}
    return result
def remove_from_dict(data: dict, key_criteria) -> tuple[dict]:
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary.")
    filtered = {k: v for k, v in data.items() if not key_criteria(k)}
    return filtered
def main():
    sample_list = [10, 20, 30, 'a', 'b']
    def is_even(item):
        return isinstance(item, int) and item % 2 == 0
    result_list = remove_from_list(sample_list.copy(), is_even)
    sample_set = {1, 3, 5, 'x', 'y'}
    def is_odd_or_x(item):
        return isinstance(item, int) and item % 2 == 1 or item == 'x'
    result_set = remove_from_set(sample_set.copy(), is_odd_or_x)
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    def starts_with_a(key):
        return key.startswith('a')
    result_dict = remove_from_dict(sample_dict.copy(), starts_with_a)
if __name__ == '__main__':
    main()