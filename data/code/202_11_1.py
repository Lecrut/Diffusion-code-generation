def find_largest(numbers):
    return max(numbers)
if __name__ == '__main__':
    data1 = [10, 5, 20, 8]
    result1 = find_largest(data1)
    print(result1)
    data2 = [-5, -1, -10, -3]
    result2 = find_largest(data2)
    print(result2)
    data3 = [3.14, 2.71, 1.618]
    result3 = find_largest(data3)
    print(result3)
    data4 = [42]
    result4 = find_largest(data4)
    print(result4)