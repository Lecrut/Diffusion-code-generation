def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 > sum2:
        return list1
    elif sum2 > sum1:
        return list2
    else:
        return "Sums are equal"
if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [5, 15, 25, 35]
    result = compare_list_sums(list_a, list_b)
    print(result)