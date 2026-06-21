def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data = [15, 25, 5, 35, 45, 15, 25]
    print(find_largest(sample_data))