def find_largest_value(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4, 5, 6, 7, 8, 9, 0]
    print(find_largest_value(sample_data))