def find_largest(numbers):
    if not numbers:
        raise ValueError('List cannot be empty')
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    data1 = [10, 5, 20, 8]
    result1 = find_largest(data1)
    print(result1)
    data2 = [-5, -1, -10, -3]
    result2 = find_largest(data2)
    print(result2)
    data3 = [42]
    result3 = find_largest(data3)
    print(result3)
    data4 = [7]
    result4 = find_largest(data4)
    print(result4)