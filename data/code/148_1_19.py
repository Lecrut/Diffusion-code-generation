def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_numbers = [72, 34, 89, 65, 12, 98, 45, 76, 54, 32]
    result = find_largest(sample_numbers)
    print(result)