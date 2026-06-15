def compare_sets(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 > sum2:
        result = {"sum1": sum1, "greater_list": "list1"}
    elif sum2 > sum1:
        result = {"sum2": sum2, "greater_list": "list2"}
    else:
        result = {"sum1": sum1, "sum2": sum2, "equal": True}
    return result
if __name__ == '__main__':
    list_a = [1, 5, 3, 7]
    list_b = [2, 4, 1, 8]
    list_c = [10, 20, 30]
    list_d = [5, 5]
    print(compare_sets(list_a, list_b))
    print(compare_sets(list_c, list_d))
    print(compare_sets(list_a, list_a))