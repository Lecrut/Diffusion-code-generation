def compare_magnitude_difference(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    return abs(sum1 - sum2)
if __name__ == '__main__':
    list_a = [1, 5, 3]
    list_b = [4, 2, 6]
    result = compare_magnitude_difference(list_a, list_b)
    print(result)