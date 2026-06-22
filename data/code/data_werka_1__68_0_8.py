def sum_of_differences(list1, list2):
    min_length = min(len(list1), len(list2))
    sum_diff = 0
    for i in range(min_length):
        sum_diff += abs(list1[i] - list2[i])
    return sum_diff
if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5, 15, 25, 35, 45]
    result = sum_of_differences(list1, list2)
    print(result)