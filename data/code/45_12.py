def find_lowest_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    lowest = numbers[0]
    for number in numbers[1:]:
        if number < lowest:
            lowest = number
    return lowest

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 0.7, 2.3, 5.1, 0.1]
    result = find_lowest_value(sample_values)
    print(result)