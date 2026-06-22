def find_lowest_value(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    lowest = numbers[0]
    for number in numbers[1:]:
        if number < lowest:
            lowest = number
    return lowest

if __name__ == '__main__':
    sample_data = [3.14, 2.71, 9.81, 0.5, 4.0, -1.25, 0.0]
    result = find_lowest_value(sample_data)
    print(result)