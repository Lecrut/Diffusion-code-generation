def compare_lists(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        if list1[i] > list2[i]:
            result.append("list1")
        elif list2[i] > list1[i]:
            result.append("list2")
        else:
            result.append("equal")
    return result
if __name__ == '__main__':
    list_a = [1, 5, 3, 8, 2]
    list_b = [4, 2, 6, 7, 1]
    comparison_result = compare_lists(list_a, list_b)
    print(comparison_result)