def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2, 9, 4]
    print(find_largest(sample_numbers))