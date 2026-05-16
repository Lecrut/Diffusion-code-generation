def compare_elements(list1, list2, index):
    return list1[index] <= list2[index]
if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [15, 25, 35]
    idx = 1
    result = compare_elements(list_a, list_b, idx)
    print(result)
    list_c = [5, 100, 150]
    list_d = [5, 99, 150]
    idx = 1
    result = compare_elements(list_c, list_d, idx)
    print(result)
    list_e = [1, 2, 3]
    list_f = [4, 5, 6]
    idx = 0
    result = compare_elements(list_e, list_f, idx)
    print(result)