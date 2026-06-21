from functools import cmp_to_key

def list_sum(a, b):
    return sum(a) - sum(b)

def sort_lists_by_sum(lists):
    key = cmp_to_key(list_sum)
    return sorted(lists, key=key)

if __name__ == '__main__':
    sample_lists = [[3, 2], [1, 4], [5]]
    print(sort_lists_by_sum(sample_lists))