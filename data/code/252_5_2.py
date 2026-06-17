def compare_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    return sum1 == sum2
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [10, 20, 30, 40, 50]
    result = compare_sums(list_a, list_b)
    print(result)