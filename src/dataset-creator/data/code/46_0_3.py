import time
def find_differences(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    only_in_a = [item for item in list_a if item not in set_b]
    only_in_b = [item for item in list_b if item not in set_a]
    common_elements = sorted(set_a.intersection(set_b))
    return {
        "only_in_first": only_in_a,
        "only_in_second": only_in_b,
        "common": common_elements
    }
if __name__ == '__main__':
    list1 = [3, 5, 7, 9, 2]
    list2 = [4, 6, 8, 3, 10]
    start_time = time.time()
    result = find_differences(list1, list2)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print("Only in first:", result["only_in_first"])
    print("Only in second:", result["only_in_second"])
    print("Common elements:", result["common"])