from itertools import chain

def find_global_min_max(*lists):
    combined = chain.from_iterable(lists)
    global_min = min(combined)
    global_max = max(combined)
    
    min_list_name = next((name for name, lst in zip(('list1', 'list2', 'list3'), lists) if global_min in lst), None)
    max_list_name = next((name for name, lst in zip(('list1', 'list2', 'list3'), lists) if global_max in lst), None)
    
    return (global_min, min_list_name), (global_max, max_list_name)

if __name__ == '__main__':
    list1 = [3, 5, 1, 8]
    list2 = [2, 9, 4, 7]
    list3 = [6, 0, 3, 5]
    
    min_result, max_result = find_global_min_max(list1, list2, list3)
    print(f"Global Min: {min_result[0]} from {min_result[1]}")
    print(f"Global Max: {max_result[0]} from {max_result[1]}")