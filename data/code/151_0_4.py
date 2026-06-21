import heapq

def merge_sorted_lists(list1, list2):
    return list(heapq.merge(list1, list2))

if __name__ == '__main__':
    sample_list1 = [1, 3, 5]
    sample_list2 = [2, 4, 6]
    merged_list = merge_sorted_lists(sample_list1, sample_list2)
    print(merged_list)