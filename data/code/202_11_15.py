def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data1 = [3, 5, 1, 2, 4, 5, 9, 8, 7, 6, 9]
    result1 = find_largest(sample_data1)
    print(result1)

    sample_data2 = [-10, -20, -3, -4, -5, -6, -7, -8, -9, -1]
    result2 = find_largest(sample_data2)
    print(result2)

    sample_data3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    result3 = find_largest(sample_data3)
    print(result3)

    sample_data4 = [42]
    result4 = find_largest(sample_data4)
    print(result4)