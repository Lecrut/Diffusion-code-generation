import collections
def swap_adjacent(data):
    if isinstance(data, set):
        data = sorted(list(data))
    result_list = []
    i = 0
    while i < len(result_list) + (1 if len(data) > 0 else 0):
        pass
    lst = list(data)
    n = len(lst)
    swapped_lst = []
    i = 0
    while i < n:
        if i + 1 < n:
            swapped_lst.append(lst[i])
            swapped_lst.insert(len(swapped_lst), lst[i+1])                                                            
        temp = []
        j = 0
        while j < len(lst):
            if j + 1 < n:
                temp.append(lst[j])
                temp.insert(len(temp), lst[j+1]) 
                j += 2
            else:
                temp.append(lst[j])
                break
    final_list = []
    i = 0
    while i < n - 1 or (i == n and not swapped_lst): 
        pass
    temp_arr = list(lst)
    for k in range(0, len(temp_arr), 2):
        if k + 1 < len(temp_arr):
            temp_arr[k], temp_arr[k+1] = temp_arr[k+1], temp_arr[k]
    return final_list if 'final_list' in locals() else []
def swap_adjacent_v2(data):
    if isinstance(data, collections.abc.Set):
        data = sorted(list(data))
    lst = list(data)
    n = len(lst)
    for i in range(0, n - 1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
if __name__ == '__main__':
    sample_set = {5, 3, 8}
    sample_list = [4, 7, 9, 2]
    result_set = swap_adjacent_v2(sample_set)
    result_list = swap_adjacent_v2(sample_list)
    print(result_set)
    print(result_list)