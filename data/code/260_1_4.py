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
    set_a = [1, 5, 3, 7]
    set_b = [2, 4, 6, 8]
    result1 = compare_sets(set_a, set_b)
    print(result1)
    set_c = [10, 20]
    set_d = [5, 5, 5]
    result2 = compare_sets(set_c, set_d)
    print(result2)
    set_e = [1, 2, 3]
    set_f = [4, 5, 6]
    result3 = compare_sets(set_e, set_f)
    print(result3)