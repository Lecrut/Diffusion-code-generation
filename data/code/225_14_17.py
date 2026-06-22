import itertools

def find_global_min_max(*lists):
    combined = list(itertools.chain.from_iterable(lists))
    global_min = min(combined)
    global_max = max(combined)
    
    min_info = [(name, min_val) for name, min_val in zip(lists, [min(lst) for lst in lists]) if min_val == global_min]
    max_info = [(name, max_val) for name, max_val in zip(lists, [max(lst) for lst in lists]) if max_val == global_max]
    
    return (global_min, min_info), (global_max, max_info)

if __name__ == '__main__':
    list1 = [3, 5, 1, 2]
    list2 = [8, 4, 6, 7]
    list3 = [0, 9, 3, 5]

    min_result, max_result = find_global_min_max(list1, list2, list3)
    
    print("Global Min:", min_result)
    print("Global Max:", max_result)