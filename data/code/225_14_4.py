import itertools

def find_global_min_max(*lists):
    combined = list(itertools.chain.from_iterable(lists))
    global_min = min(combined)
    global_max = max(combined)
    
    min_list = next((name for name, lst in zip(('list1', 'list2', 'list3'), lists) if global_min in lst), None)
    max_list = next((name for name, lst in zip(('list1', 'list2', 'list3'), lists) if global_max in lst), None)
    
    return (global_min, min_list), (global_max, max_list)

if __name__ == '__main__':
    list1 = [3, 5, 1, 8]
    list2 = [7, 2, 9, 4]
    list3 = [6, 0, 10, 3]
    
    min_result, max_result = find_global_min_max(list1, list2, list3)
    print("Global Min:", min_result)
    print("Global Max:", max_result)