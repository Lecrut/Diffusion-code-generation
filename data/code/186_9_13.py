from functools import cmp_to_key

def compare_lists(list1, list2):
    return sum(list1) - sum(list2)

def sort_list_of_lists(lst):
    key = cmp_to_key(compare_lists)
    return sorted(lst, key=key)

if __name__ == '__main__':
    sample_data = [[3, 5], [1, 2], [4, 6]]
    print(sort_list_of_lists(sample_data))