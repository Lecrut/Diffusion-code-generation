def find_lowest_value(numbers):
    if not numbers:
        return None
    lowest = numbers[0]
    for number in numbers[1:]:
        if number < lowest:
            lowest = number
    return lowest

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 0.9, 2.3, -1.1, 5.6]
    result = find_lowest_value(sample_values)
    print(result)