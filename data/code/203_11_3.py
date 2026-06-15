import math
def compare_quantities(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    difference = sum1 - sum2
    if sum1 > sum2:
        greater = "list1"
    elif sum2 > sum1:
        greater = "list2"
    else:
        greater = "equal"
    return {
        "sum1": sum1,
        "sum2": sum2,
        "difference": difference,
        "greater": greater
    }
if __name__ == '__main__':
    data1 = [10, 20, 30, 40]
    data2 = [5, 15, 25, 35]
    result = compare_quantities(data1, data2)
    print(result)