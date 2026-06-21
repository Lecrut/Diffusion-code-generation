def find_largest_value(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data = [3, 5, 1, 8, 2, 8, 4, 7, 6, 9, 0]
    print(find_largest_value(sample_data))