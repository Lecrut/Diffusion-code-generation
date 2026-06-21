def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data = [15, 25, 10, 30, 20, 40, 35, 50]
    print(find_largest(sample_data))