def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

if __name__ == '__main__':
    list_a = [1, 3, 5, 7]
    list_b = [2, 4, 6, 8]
    result1 = merge_sorted_lists(list_a, list_b)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Merged List: {result1}")

    list_c = [10, 20, 30]
    list_d = [25, 35, 45]
    result2 = merge_sorted_lists(list_c, list_d)
    print(f"\nList C: {list_c}")
    print(f"List D: {list_d}")
    print(f"Merged List: {result2}")