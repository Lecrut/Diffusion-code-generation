import time
def remove_from_list(items: list, criteria_func) -> list:
    return [item for item in items if not criteria_func(item)]
def remove_from_set(items: set, criteria_func) -> set:
    new_items = {item for item in items if not criteria_func(item)}
    return new_items
def remove_from_dict(data: dict, key_criteria_func, value_criteria_func=None) -> dict:
    if value_criteria_func is None:
        return {k for k in data.keys() if not key_criteria_func(k)}
    else:
        result = {}
        for k, v in data.items():
            if not (key_criteria_func(k) and value_criteria_func(v)):
                result[k] = v
        return result
def main():
    list_data = [10, 20, 30, 'a', 'b', None, True]
    def is_even(x):
        if isinstance(x, int):
            return x % 2 == 0
        return False
    def starts_with_a(s):
        if isinstance(s, str):
            return s.startswith('a')
        return False
    filtered_list = remove_from_list(list_data.copy(), lambda x: is_even(x) or starts_with_a(str(x)))
    set_data = {1, 2, 3, 4, 5}
    def is_odd(n):
        return n % 2 != 0
    filtered_set = remove_from_set(set_data.copy(), lambda x: is_odd(x))
    dict_data = {'a': 1, 'b': 2, 'c': 3}
    def key_is_a(k):
        return k == 'a' or k.startswith('b')
    filtered_dict = remove_from_dict(dict_data.copy(), lambda x: key_is_a(x))
if __name__ == '__main__':
    pass