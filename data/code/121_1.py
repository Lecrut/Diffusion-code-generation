def compare_quantities(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 > sum2:
        return (list1, "list1")
    elif sum2 > sum1:
        return (list2, "list2")
    else:
        return (list1, "equal")
if __name__ == '__main__':
    data1 = [10, 20, 30]
    data2 = [5, 15, 25]
    result1 = compare_quantities(data1, data2)
    print(result1)
    data3 = [1, 2, 3]
    data4 = [4, 5, 6]
    result2 = compare_quantities(data3, data4)
    print(result2)
    data5 = [100]
    data6 = [50, 60]
    result3 = compare_quantities(data5, data6)
    print(result3)