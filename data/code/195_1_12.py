def find_first_mismatch(list1, list2):
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        if list1[i] != list2[i]:
            return i
    if len(list1) != len(list2):
        return min_length
    return -1
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 4]
    list_c = [1, 2, 9, 4]
    print(find_first_mismatch(list_a, list_b))
    print(find_first_mismatch(list_a, list_c))