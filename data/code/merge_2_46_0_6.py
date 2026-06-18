import time
def find_list_differences(list1: list, list2: list) -> tuple[list, set]:
    diff_ordered = [x for x in list1 if x not in list2]
    diff_set = {x for x in list1 if x not in list2}
    return diff_ordered, diff_set
def find_symmetric_difference(list1: list, list2: list) -> set:
    set1 = set(list1)
    set2 = set(list2)
    return (set1 - set2) | (set2 - set1)
def find_intersection(list1: list, list2: list) -> set:
    return set(list1).intersection(set(list2))
if __name__ == '__main__':
    data_a = [i * 5 for i in range(10_000)] + list(range(1, 6))
    data_b = [(i - 2) * 5 for i in range(9_800)] + list(range(4, 10))
    start_time = time.time()
    ordered_diff, unique_diff = find_list_differences(data_a, data_b)
    symmetric_diff = find_symmetric_difference(data_a, data_b)
    intersection_res = find_intersection(data_a, data_b)
    print(f"Ordered differences: {ordered_diff[:5]}... (Total count: {len(ordered_diff)})")
    print(f"Unique differences: {unique_diff}")
    print(f"Symmetric difference size: {len(symmetric_diff)}")
    print(f"Intersection size: {len(intersection_res)}")
    end_time = time.time()
    elapsed = end_time - start_time
    pass