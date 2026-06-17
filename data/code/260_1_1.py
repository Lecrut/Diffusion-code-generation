import time
def compare_sets(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 > sum2:
        result = {"sum1": sum1, "winner": "list1"}
    elif sum2 > sum1:
        result = {"sum1": sum1, "winner": "list2"}
    else:
        result = {"sum1": sum1, "winner": "tie"}
    return result
if __name__ == '__main__':
    list_a = [1, 5, 9, 3]
    list_b = [2, 4, 6, 8]
    print(compare_sets(list_a, list_b))
    list_c = [10, 20, 30]
    list_d = [5, 5, 5]
    print(compare_sets(list_c, list_d))
    list_e = [1, 2, 3]
    list_f = [4, 5, 6]
    print(compare_sets(list_e, list_f))