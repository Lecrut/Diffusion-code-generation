def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 == sum2:
        return "Sums are equal"
    else:
        return "Sums are not equal"
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [5, 10, 15, -5]
    result = compare_list_sums(list_a, list_b)
    print(result)