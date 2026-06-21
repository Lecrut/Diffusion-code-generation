def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_numbers = [34, 78, 12, 90, 56, 23, 89, 45, 67, 10, 33, 77, 22, 66, 44, 88, 55, 99, 11, 76, 32, 65, 43, 87, 54, 98, 13, 75, 31, 64, 42, 86, 53, 97, 14, 74, 30, 63, 41, 85, 52, 96, 15, 73, 29, 62, 40, 84, 51]
    print(find_largest(sample_numbers))