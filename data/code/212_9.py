def compare_lists(list1, list2):
    min1 = min(list1)
    max1 = max(list1)
    sum1 = sum(list1)
    min2 = min(list2)
    max2 = max(list2)
    sum2 = sum(list2)
    return {
        "list1": {"min": min1, "max": max1, "sum": sum1},
        "list2": {"min": min2, "max": max2, "sum": sum2}
    }
if __name__ == '__main__':
    list_a = [10, 5, 20, 15]
    list_b = [3, 8, 1, 12]
    result = compare_lists(list_a, list_b)
    print(result)