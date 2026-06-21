def validate_sorted_lists(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise ValueError("Both inputs must be lists.")
    if not all(isinstance(x, (int, float)) for x in list1 + list2):
        raise ValueError("All elements in both lists must be numbers.")

def merge_sorted_lists(list1, list2):
    validate_sorted_lists(list1, list2)
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result1 = merge_sorted_lists(list_a, list_b)
    print(f"Merged List: {result1}")
    list_c = [10, 20, 30]
    list_d = [30, 40, 50]
    result2 = merge_sorted_lists(list_c, list_d)
    print(f"Merged List: {result2}")