def find_largest(numbers):
    return max(numbers)
if __name__ == '__main__':
    data1 = [10, 5, 20, 8]
    data2 = [-5, -1, -10, -3]
    data3 = [42]
    data4 = [7]
    print(find_largest(data1))
    print(find_largest(data2))
    print(find_largest(data3))
    print(find_largest(data4))