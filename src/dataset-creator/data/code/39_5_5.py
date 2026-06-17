import heapq
def find_max_across_lists(*lists):
    if not any(lists):
        raise ValueError("At least one list must be provided.")
    max_item = float('-inf')
    for lst in lists:
        if not isinstance(lst, (list, tuple)):
            continue
        for item in lst:
            try:
                val = int(item)
            except TypeError:
                raise ValueError("All items must be integers.")
            if val > max_item:
                max_item = val
    return max_item
if __name__ == '__main__':
    list_a = [10, 5, 23]
    list_b = [-1, 45, 9]
    list_c = [78, -100, 60]
    result = find_max_across_lists(list_a, list_b, list_c)
    print(result)