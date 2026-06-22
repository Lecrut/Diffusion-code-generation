def find_lowest(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    lowest = numbers[0]
    for number in numbers[1:]:
        if number < lowest:
            lowest = number
    return lowest

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.41, 4.56, 0.99, 5.0]
    result = find_lowest(sample_values)
    print(result)