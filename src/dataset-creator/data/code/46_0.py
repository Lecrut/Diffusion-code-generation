import time
def find_differences(list1, list2):
    set1 = set(map(str.strip, [str(x) for x in list1]))
    set2 = set(map(str.strip, [str(x) for x in list2]))
    only_in_list1 = sorted(set1 - set2)
    only_in_list2 = sorted(set2 - set1)
    return {
        'only_in_first': only_in_list1,
        'only_in_second': only_in_list2,
        'common_elements': sorted(list(set1 & set2))
    }
if __name__ == '__main__':
    list_a = [3, 5, 7, 9, 10]
    list_b = [4, 6, 8, 10, 12]
    start_time = time.time()
    result = find_differences(list_a, list_b)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print("Elements only in first list:", result['only_in_first'])
    print("Elements only in second list:", result['only_in_second'])