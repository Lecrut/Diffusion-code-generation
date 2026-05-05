def compare_elements(list1, list2, index):
    return list1[index] <= list2[index]
if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [15, 25, 35]
    idx = 1
    result = compare_elements(list_a, list_b, idx)
    print(result)