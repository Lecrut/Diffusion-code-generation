import time
def compare_and_find_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    symmetric_difference = set1.symmetric_difference(set2)
    return intersection, symmetric_difference
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5, 6]
    list_b = [4, 5, 6, 7, 8, 1]
    start_time = time.perf_counter()
    common, diff = compare_and_find_difference(list_a, list_b)
    end_time = time.perf_counter()
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Intersection (Elements in both): {list(common)}")
    print(f"Symmetric Difference (Elements unique to either list): {list(diff)}")
    print(f"Execution Time: {(end_time - start_time) * 1000:.6f} ms")