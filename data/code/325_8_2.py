import time
def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    symmetric_difference = set1.symmetric_difference(set2)
    return intersection, symmetric_difference
if __name__ == '__main__':
    list_a = list(range(0, 1000000))
    list_b = list(range(500000, 1500000))
    start_time = time.perf_counter()
    intersection_set, symmetric_difference_set = compare_lists(list_a, list_b)
    end_time = time.perf_counter()
    print(f"Intersection size: {len(intersection_set)}")
    print(f"Symmetric Difference size: {len(symmetric_difference_set)}")
    print(f"Time taken: {(end_time - start_time):.6f} seconds")