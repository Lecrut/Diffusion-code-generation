def compare_sets(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 > sum2:
        return {"sum1": sum1, "greater_list": "list1"}
    elif sum2 > sum1:
        return {"sum1": sum1, "greater_list": "list2"}
    else:
        return {"sum1": sum1, "greater_list": "equal"}
if __name__ == '__main__':
    list_a = [1, 5, 3, 7]
    list_b = [2, 4, 6, 1]
    result = compare_sets(list_a, list_b)
    print(result)