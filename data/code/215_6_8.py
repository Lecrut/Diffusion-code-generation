def find_largest_number(numbers):
    largest = float('-inf')
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_numbers = [3.14, 2.71, 1.41, 9.81, 6.28]
    result = find_largest_number(sample_numbers)
    print(result)