from functools import cmp_to_key

def sum_lists(list1, list2):
    return (sum(list1) - sum(list2))

def sort_list_of_lists(lst):
    key_func = cmp_to_key(sum_lists)
    lst.sort(key=key_func)
    return lst

if __name__ == '__main__':
    sample_data = [[3, 2], [1, 4], [5]]
    sorted_data = sort_list_of_lists(sample_data)
    print(sorted_data)