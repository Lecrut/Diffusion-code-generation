def compare_elements(list1, list2, index):
    return list1[index] <= list2[index]
if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [15, 25, 35]
    idx = 1
    result = compare_elements(list_a, list_b, idx)
    print(result)
    list_c = [5, 100]
    list_d = [4, 101]
    idx = 0
    result = compare_elements(list_c, list_d, idx)
    print(result)
    list_e = [50, 60]
    list_f = [55, 59]
    idx = 0
    result = compare_elements(list_e, list_f, idx)
    print(result)