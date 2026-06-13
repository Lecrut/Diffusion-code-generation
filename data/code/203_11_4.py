def compare_quantities(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    difference = sum1 - sum2
    if sum1 > sum2:
        greater = "list1"
    elif sum2 > sum1:
        greater = "list2"
    else:
        greater = "equal"
    return {
        "sum_list1": sum1,
        "sum_list2": sum2,
        "difference": difference,
        "greater": greater
    }
if __name__ == '__main__':
    a = [10, 20, 30]
    b = [5, 15, 25]
    result = compare_quantities(a, b)
    print(result)