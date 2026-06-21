def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [34, 78, 12, 90, 56, 23, 89, 67, 45, 32, 76, 18, 54, 98, 29, 65, 37, 83, 48, 52,
                     10, 72, 31, 64, 28, 92, 50, 85, 42, 39, 71, 15, 58, 95, 26, 63, 35, 88, 44, 51,
                     11, 74, 30, 62, 27, 93, 55, 86, 41, 38]
    print(find_largest(sample_values))