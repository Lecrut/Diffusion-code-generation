MIN_VALUE = float('-inf')
MAX_VALUE = float('inf')

def union_range(list1, list2):
    combined_set = set(list1 + list2)
    return (min(combined_set, default=MIN_VALUE), max(combined_set, default=MAX_VALUE))

if __name__ == '__main__':
    sample_list1 = [3, 5, 7, 9]
    sample_list2 = [2, 4, 6, 8, 9]
    print(union_range(sample_list1, sample_list2))