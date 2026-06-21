def find_lowest_number(numbers):
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest

if __name__ == '__main__':
    sample_numbers = [4, 7, 1, 3, 9, 2]
    print(find_lowest_number(sample_numbers))