from functools import cmp_to_key

def sum_of_elements(list1, list2):
    return sum(list1) - sum(list2)

def sort_lists_by_sum(lists):
    key = cmp_to_key(sum_of_elements)
    return sorted(lists, key=key)

if __name__ == '__main__':
    sample_lists = [[3, 5, 1], [1, 2], [4, 6]]
    sorted_lists = sort_lists_by_sum(sample_lists)
    print(sorted_lists)