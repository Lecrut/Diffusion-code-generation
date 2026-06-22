def find_lowest_value(numbers):
    if not numbers:
        raise ValueError("List is empty")
    lowest = numbers[0]
    for num in numbers[1:]:
        if num < lowest:
            lowest = num
    return lowest

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 0.9, 2.3]
    result = find_lowest_value(sample_values)
    print(result)