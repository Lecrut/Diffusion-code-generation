def find_largest_value(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = (1.414, 2.718, 3.14159, 2.30259)
    print(find_largest_value(sample_values))