def find_lowest(numbers):
    if not numbers:
        return None
    lowest = numbers[0]
    for num in numbers[1:]:
        if num < lowest:
            lowest = num
    return lowest

if __name__ == '__main__':
    sample_data = [3.5, 1.2, 9.8, 0.5, 7.4, -2.1, 4.0]
    result = find_lowest(sample_data)
    print(result)