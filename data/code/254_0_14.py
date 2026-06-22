def find_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

if __name__ == '__main__':
    data1 = [7, 23, 45, -1, 0, 89, 6]
    result1 = find_minimum(data1)
    print(result1)

    data2 = [-3, -5, -2, -8, -10]
    result2 = find_minimum(data2)
    print(result2)

    data3 = [100]
    result3 = find_minimum(data3)
    print(result3)