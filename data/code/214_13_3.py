def find_lowest_number(numbers):
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 1, 8, 3, 6]
    print(find_lowest_number(sample_numbers))