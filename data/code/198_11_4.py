def find_smallest(numbers):
    return min(numbers)
if __name__ == '__main__':
    data1 = [3, 1, 4, 1, 5, 9, 2]
    result1 = find_smallest(data1)
    print(result1)
    data2 = [-10, 0, 5, -20, 3]
    result2 = find_smallest(data2)
    print(result2)
    data3 = [42]
    result3 = find_smallest(data3)
    print(result3)
    data4 = [-5, -1, -100]
    result4 = find_smallest(data4)
    print(result4)