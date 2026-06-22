import itertools

def find_global_min_max(*lists):
    combined = list(itertools.chain.from_iterable(lists))
    global_min = min(combined)
    global_max = max(combined)
    
    min_list_name, max_list_name = None, None
    for name, lst in zip(('list1', 'list2', 'list3'), lists):
        if all(x == global_min for x in lst):
            min_list_name = name
        if any(x == global_max for x in lst):
            max_list_name = name
    
    return (global_min, min_list_name), (global_max, max_list_name)

if __name__ == '__main__':
    list1 = [3, 5, 1, 2]
    list2 = [4, 6, 0, 8]
    list3 = [7, 9, 3, 10]
    
    min_result, max_result = find_global_min_max(list1, list2, list3)
    print(f"Global Min: {min_result[0]} from {min_result[1]}")
    print(f"Global Max: {max_result[0]} from {max_result[1]}")