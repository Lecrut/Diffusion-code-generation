def find_lowest_number(numbers):
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest

if __name__ == '__main__':
    sample_numbers = [34, 78, 12, 56, 90, 23, 10]
    print(find_lowest_number(sample_numbers))