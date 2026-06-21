import heapq

def merge_sorted_lists(list1, list2):
    return list(heapq.merge(list1, list2))

if __name__ == '__main__':
    list_a = [1, 3, 5, 7]
    list_b = [2, 4, 6, 8]
    result = merge_sorted_lists(list_a, list_b)
    print(f"Merged List: {result}")