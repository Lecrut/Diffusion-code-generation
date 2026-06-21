import heapq

def merge_sorted_lists(list1, list2):
    if not all(isinstance(item, (int, float)) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers or floats.")
    return list(heapq.merge(list1, list2))

if __name__ == '__main__':
    list_a = [1, 3, 5, 7]
    list_b = [2, 4, 6, 8]
    result1 = merge_sorted_lists(list_a, list_b)
    print(f"Merged List: {result1}")
    
    list_c = [1.1, 2.2, 3.3]
    list_d = [2.2, 3.3, 4.4]
    result2 = merge_sorted_lists(list_c, list_d)
    print(f"Merged List: {result2}")