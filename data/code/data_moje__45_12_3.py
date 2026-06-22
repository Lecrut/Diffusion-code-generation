def find_lowest(numbers):
    if not numbers:
        return None
    lowest = numbers[0]
    for num in numbers[1:]:
        if num < lowest:
            lowest = num
    return lowest

if __name__ == '__main__':
    sample_numbers = [3.5, 1.2, 4.8, 0.9, 2.7, -1.5, 3.3]
    result = find_lowest(sample_numbers)
    print(result)