def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [34, 78, 12, 90, 56, 23, 89, 67, 45, 11,
                     33, 77, 11, 99, 55, 22, 88, 66, 44, 10,
                     32, 76, 10, 98, 54, 21, 87, 65, 43, 12,
                     31, 75, 9, 97, 53, 20, 86, 64, 42, 13,
                     30, 74, 8, 96, 52, 19, 85, 63, 41, 14]
    print(find_largest(sample_values))