def compare_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    return sum1 > sum2
if __name__ == '__main__':
    array_a = [1.5, 2.0, 3.5]
    array_b = [4.0, 1.0, 0.5]
    result = compare_sums(array_a, array_b)
    print(result)