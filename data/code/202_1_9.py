def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = (2.718, 3.14159, 2.171828, 1.61803)
    print(find_largest(sample_values))