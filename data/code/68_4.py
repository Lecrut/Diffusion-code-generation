def list_difference(list1, list2):
    result = {}
    for i in range(min(len(list1), len(list2))):
        result[i] = list1[i] - list2[i]
    return result
if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [2, 5, 10, 15]
    difference_dict = list_difference(list_a, list_b)
    print(difference_dict)