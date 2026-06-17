from collections import defaultdict
import timeit
def filter_by_condition(data: list, condition_func) -> dict:
    filtered = {}
    for item in data:
        if condition_func(item):
            key = 'special' if isinstance(item[0], int) else 'general'
            filtered.setdefault(key, []).append(item)
    return filtered
def remove_duplicates_preserve_order(items: list) -> list:
    seen = set()
    result = []
    for item in items:
        if id(item) not in seen:                                                   
            seen.add(id(item))
            result.append(item)
    return result
def process_data():
    sample_list = [
        (1, 'apple'),
        (2, 'banana'),
        (3, 'cherry'),
        (4, 'date'),
        (5, 'elderberry')
    ]
    filtered_data = filter_by_condition(sample_list, lambda x: x[0] % 2 == 0 and not isinstance(x[1], str))
    return sample_list
if __name__ == '__main__':
    data = process_data()