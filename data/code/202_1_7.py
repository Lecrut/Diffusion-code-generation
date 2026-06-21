def find_largest_value(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = (3.5, 2.1, 4.8, 1.9, 5.6)
    print(find_largest_value(sample_values))