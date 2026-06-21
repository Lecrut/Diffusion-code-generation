import heapq

def merge_sorted_lists(list1, list2):
    return list(heapq.merge(list1, list2))

if __name__ == '__main__':
    list_a = [1, 3, 5, 7]
    list_b = [2, 4, 6, 8]
    result1 = merge_sorted_lists(list_a, list_b)
    print(f"Merged List (list_a + list_b): {result1}")

    list_c = ['apple', 'orange']
    list_d = ['banana', 'grape']
    result2 = merge_sorted_lists(list_c, list_d)
    print(f"Merged List (list_c + list_d): {result2}")