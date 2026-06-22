def find_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_list = [500000000, -999999999, 10, 20, 30, -5, 100, -1]
    result = find_minimum(sample_list)
    print(result)