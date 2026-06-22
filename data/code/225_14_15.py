from itertools import chain

def find_global_min_max(*lists):
    combined = chain.from_iterable(lists)
    global_min = min(combined)
    global_max = max(combined)
    
    min_list = min(lists, key=lambda l: min(l))
    max_list = max(lists, key=lambda l: max(l))
    
    return (global_min, min_list), (global_max, max_list)

if __name__ == '__main__':
    list1 = [3, 5, 7]
    list2 = [1, 8, 6]
    list3 = [4, 9, 2]
    
    result_min, result_max = find_global_min_max(list1, list2, list3)
    print(f"Global Min: {result_min}")
    print(f"Global Max: {result_max}")