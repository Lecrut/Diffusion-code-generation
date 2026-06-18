def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    result = {
        "sum1": sum1,
        "sum2": sum2,
        "comparison": "equal" if sum1 == sum2 else ("greater" if sum1 > sum2 else "less")
    }
    return result
if __name__ == '__main__':
    list_a = [1, 2.5, 3, 4.0]
    list_b = [5, -1.5, 6, 0.5]
    comparison_result = compare_list_sums(list_a, list_b)
    print(comparison_result)