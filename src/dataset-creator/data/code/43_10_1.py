import time
def remove_from_list(items: list, criteria_func) -> list:
    return [item for item in items if not criteria_func(item)]
def remove_from_set(items: set, criteria_func) -> set:
    new_items = {item for item in items if not criteria_func(item)}
    return new_items
def remove_from_dict(data: dict, key_criteria_func) -> dict:
    filtered_data = {}
    for k, v in data.items():
        if not key_criteria_func(k):
            filtered_data[k] = v
    return filtered_data
def main():
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def is_even(n):
        return n % 2 == 0
    cleaned_list = remove_from_list(sample_list.copy(), is_even)
    sample_set = {'hi', 'hello', 'a', 'world', 'python'}
    def has_short_word(s):
        return len(s) < 3
    cleaned_set = remove_from_set(sample_set.copy(), has_short_word)
    sample_dict = {'01': 'one', 'a': 'alpha', '2': 'two', 'b': 'beta'}
    def starts_with_zero(k):
        return k.startswith('0') and k.isdigit()
    cleaned_dict = remove_from_dict(sample_dict.copy(), starts_with_zero)
if __name__ == '__main__':
    pass