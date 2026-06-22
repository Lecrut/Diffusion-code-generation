def find_lowest(numbers):
    if not numbers:
        return None
    lowest = numbers[0]
    for num in numbers[1:]:
        if num < lowest:
            lowest = num
    return lowest

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.1, 5.9, 0.3]
    print(find_lowest(sample_values))