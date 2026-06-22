def find_lowest_value(numbers):
    if not numbers:
        return None
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest

if __name__ == '__main__':
    sample_data = [3.5, 1.2, 9.8, -4.3, 0.0, 7.1]
    result = find_lowest_value(sample_data)
    print(result)