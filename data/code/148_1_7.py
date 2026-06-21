def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_numbers = [34, 78, 12, 90, 56, 23, 89, 45, 67, 10, 34, 78, 12, 90, 56, 23, 89, 45, 67, 10,
                      34, 78, 12, 90, 56, 23, 89, 45, 67, 10, 34, 78, 12, 90, 56, 23, 89, 45, 67, 10,
                      34, 78, 12, 90, 56, 23, 89, 45, 67, 10]
    print(find_largest(sample_numbers))