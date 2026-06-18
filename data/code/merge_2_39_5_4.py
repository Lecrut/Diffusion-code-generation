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
    list1 = [3, 7, 2]
    list2 = [5, 9, 4]
    list3 = [8, 6, 10]
    result = find_max_across_lists(list1, list2, list3)
    print(result)