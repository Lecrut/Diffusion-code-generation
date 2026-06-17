def list_difference(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] - list2[i])
    return result
if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50]
    list_b = [2, 4, 6, 8, 10]
    difference = list_difference(list_a, list_b)
    print(difference)