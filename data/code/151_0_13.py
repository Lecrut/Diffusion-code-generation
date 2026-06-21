import heapq

def merge_sorted_lists(list1, list2):
    return list(heapq.merge(list1, list2))

if __name__ == '__main__':
    list_a = [1, 3, 5, 7]
    list_b = [2, 4, 6, 8]
    result1 = merge_sorted_lists(list_a, list_b)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Merged List: {result1}")

    list_c = ['apple', 'banana']
    list_d = ['cherry', 'date']
    result2 = merge_sorted_lists(list_c, list_d)
    print(f"\nList C: {list_c}")
    print(f"List D: {list_d}")
    print(f"Merged List: {result2}")