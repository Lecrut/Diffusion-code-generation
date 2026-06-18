import sys
def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 >= sum2:
        return list1
    else:
        return list2
if __name__ == '__main__':
    list_a = [10, 5, 8, 2]
    list_b = [3, 7, 1, 9]
    result = compare_list_sums(list_a, list_b)
    print(result)