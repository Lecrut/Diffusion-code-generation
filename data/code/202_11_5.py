def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    data1 = [4, 2, 9, 6, 5, 3]
    result1 = find_largest(data1)
    print(result1)

    data2 = [-7, -3, -8, -2, -5]
    result2 = find_largest(data2)
    print(result2)

    data3 = [0]
    result3 = find_largest(data3)
    print(result3)

    data4 = [100]
    result4 = find_largest(data4)
    print(result4)