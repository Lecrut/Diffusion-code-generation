def find_largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [45, 23, 78, 10, 90, 56]
    print(find_largest_number(sample_values))