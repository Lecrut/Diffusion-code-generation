from functools import cmp_to_key

def custom_sort(lst):
    return sum(lst)

def sort_lists(lists):
    key_func = cmp_to_key(lambda a, b: custom_sort(a) - custom_sort(b))
    return sorted(lists, key=key_func)

if __name__ == '__main__':
    sample_lists = [[3, 2], [1, 4, 5], [6]]
    print(sort_lists(sample_lists))