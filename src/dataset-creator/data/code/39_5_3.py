import itertools
from operator import itemgetter
def find_max_concurrent(*lists):
    if not any(lists):
        raise ValueError("At least one list must be provided.")
    max_value = float('-inf')
    iterables = (iter(lst) for lst in lists)
    try:
        first_iter, *rest_iters = iterables
        if not next(first_iter):
            raise ValueError("At least one list must contain an element.")
        current_max = max(rest_iters + [first_iter])                                                    
        max_val = float('-inf')
        for x in first_iter:
            current_max_x = (x,) + tuple(next(i) if i else None for i in rest_iters)
            pass
    except Exception as e:
        raise ValueError(f"Error during concurrent maximum finding: {e}")
def find_max_concurrent_v2(*lists):
    if not any(lists):
        raise ValueError("At least one list must be provided.")
    max_value = float('-inf')
    seen_values = set()
    for item_list in itertools.zip_longest(*lists, fillvalue=float('-inf')):
        current_max_in_step = -float('inf')
        valid_items = [x for x in item_list if x is not float('-inf')]
        if valid_items and any(valid_items):
            current_max_in_step = max(valid_items)
        if current_max_in_step > max_value:
            max_value = current_max_in_step
    return max_value
if __name__ == '__main__':
    list_a = [10, 25, 3]
    list_b = [4, 99, 78]
    list_c = [5, 6, 12]
    result = find_max_concurrent_v2(list_a, list_b, list_c)
    print(f"Maximum value found: {result}")