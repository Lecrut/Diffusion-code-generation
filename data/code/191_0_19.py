def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

if __name__ == '__main__':
    sample_list_a = [1, 3, 5, 7]
    sample_list_b = [2, 4, 6, 8]
    result = merge_sorted_lists(sample_list_a, sample_list_b)
    print(f"Merged List: {result}")