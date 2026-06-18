def compare_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 >= sum2:
        return (list1, sum1, sum2)
    else:
        return (list2, sum2, sum1)
if __name__ == '__main__':
    list_a = [1, 5, 3, 7]
    list_b = [2, 4, 1, 8]
    result = compare_sums(list_a, list_b)
    print(result)