def find_lowest_number(numbers):
    if not numbers:
        return None
    lowest = numbers[0]
    for number in numbers[1:]:
        if number < lowest:
            lowest = number
    return lowest

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 6]
    print(find_lowest_number(sample_numbers))