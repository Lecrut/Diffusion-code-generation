import functools

def compare_lists(list1, list2):
    return sum(list1) - sum(list2)

def sort_by_sum(lists):
    return sorted(lists, key=functools.cmp_to_key(compare_lists))

if __name__ == '__main__':
    sample_data = [[5, 7], [3, 9], [2, 4, 6]]
    sorted_data = sort_by_sum(sample_data)
    print(sorted_data)