def find_first_mismatch(list1, list2):
    length = min(len(list1), len(list2))
    for i in range(length):
        if list1[i] != list2[i]:
            return i
    if len(list1) != len(list2):
        return length
    return -1

if __name__ == '__main__':
    result_a_b = find_first_mismatch([1, 2, 3, 4], [1, 2, 3, 4])
    result_a_c = find_first_mismatch([1, 2, 3, 4], [1, 2, 9, 4])
    print(result_a_b)
    print(result_a_c)