def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    result = {
        "sum_list1": sum1,
        "sum_list2": sum2,
        "comparison": "equal" if sum1 == sum2 else ("list1_greater" if sum1 > sum2 else "list2_greater")
    }
    return result
if __name__ == '__main__':
    data1 = [1, 2.5, 3, 4.0]
    data2 = [5, 1.5, 7.5, 0]
    comparison_result = compare_list_sums(data1, data2)
    print(comparison_result)