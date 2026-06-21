def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [34, 12, 89, 56, 78, 23, 19, 67, 45, 90, 32, 76, 54, 88, 21, 99, 65, 33, 77, 18,
                     42, 64, 58, 92, 38, 70, 11, 83, 48, 62, 50, 95, 36, 74, 22, 91, 46, 68, 52, 93,
                     30, 72, 40, 66, 55, 94, 31, 75, 24, 96]
    print(find_largest(sample_values))