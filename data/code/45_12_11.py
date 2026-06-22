def find_lowest_value(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    lowest = numbers[0]
    for number in numbers[1:]:
        if number < lowest:
            lowest = number
    return lowest

if __name__ == '__main__':
    sample_data = [3.5, 1.2, 9.8, 0.4, 5.5, -2.1, 4.3]
    result = find_lowest_value(sample_data)
    print(result)