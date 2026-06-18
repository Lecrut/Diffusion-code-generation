def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    result = {
        "list1_sum": sum1,
        "list2_sum": sum2,
        "comparison": "equal" if sum1 == sum2 else "not equal"
    }
    return result
if __name__ == '__main__':
    data1 = [1, 2.5, 3, 4.0]
    data2 = [5, 6.5, 7, 8.0]
    comparison_result = compare_list_sums(data1, data2)
    print(comparison_result)