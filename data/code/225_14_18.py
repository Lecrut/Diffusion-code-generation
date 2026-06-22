import itertools

def find_global_min_max(*lists):
    combined = list(itertools.chain.from_iterable(lists))
    global_min = min(combined)
    global_max = max(combined)
    
    min_list_name = None
    max_list_name = None
    
    for name, lst in zip(('list1', 'list2', 'list3'), lists):
        if global_min in lst:
            min_list_name = name
            break
    
    for name, lst in zip(('list1', 'list2', 'list3'), lists):
        if global_max in lst:
            max_list_name = name
            break
    
    return (global_min, min_list_name), (global_max, max_list_name)

if __name__ == '__main__':
    list1 = [3, 5, 7]
    list2 = [2, 4, 6, 8]
    list3 = [9, 10, 11]
    
    result_min, result_max = find_global_min_max(list1, list2, list3)
    print(f"Global Min: {result_min[0]} in {result_min[1]}")
    print(f"Global Max: {result_max[0]} in {result_max[1]}")