from functools import cmp_to_key

def sum_compare(a, b):
    return sum(a) - sum(b)

def sort_lists_by_sum(lists):
    return sorted(lists, key=cmp_to_key(sum_compare))

if __name__ == '__main__':
    sample_lists = [[3, 2], [1, 4], [5]]
    print(sort_lists_by_sum(sample_lists))