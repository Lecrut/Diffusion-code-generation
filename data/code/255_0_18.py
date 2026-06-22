def find_maximum(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    data1 = [10, 5, 20, 8]
    result1 = find_maximum(data1)
    print(result1)
    data2 = [-5, -1, -10, -3]
    result2 = find_maximum(data2)
    print(result2)
    data3 = [42]
    result3 = find_maximum(data3)
    print(result3)
    data4 = []
    result4 = find_maximum(data4)
    print(result4)