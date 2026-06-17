def compare_lists(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        if list1[i] > list2[i]:
            result.append(list1[i])
        elif list2[i] > list1[i]:
            result.append(list2[i])
        else:
            result.append("Equal")
    return result
if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50]
    list_b = [5, 15, 30, 45, 60]
    comparison_result = compare_lists(list_a, list_b)
    print(comparison_result)