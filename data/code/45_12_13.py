def find_lowest_value(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    lowest = numbers[0]
    for value in numbers[1:]:
        if value < lowest:
            lowest = value
    return lowest

if __name__ == '__main__':
    sample_data = [3.5, 1.2, 8.9, 0.5, 4.7]
    result = find_lowest_value(sample_data)
    print(result)