def find_minimum(numbers):
    if not numbers:
        raise ValueError('List cannot be empty')
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    return min_value
if __name__ == '__main__':
    data1 = [3, 1, 4, 1, 5, 9, 2]
    result1 = find_minimum(data1)
    print(result1)
    data2 = [-10, 0, 5, -20, 3]
    result2 = find_minimum(data2)
    print(result2)
    data3 = [42]
    result3 = find_minimum(data3)
    print(result3)