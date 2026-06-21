import functools

def sum_elements(lst):
    return sum(lst)

def compare_lists(list1, list2):
    return sum_elements(list1) - sum_elements(list2)

def sort_by_sum(lists):
    return sorted(lists, key=functools.cmp_to_key(compare_lists))

if __name__ == '__main__':
    sample_lists = [[3, 5], [1, 2, 3], [4, 6], [7]]
    sorted_lists = sort_by_sum(sample_lists)
    print(sorted_lists)