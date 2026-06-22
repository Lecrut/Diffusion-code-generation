def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [15.7, 8.2, 22.3, 4.9, 30.5, 11.1]
    result = find_largest(sample_list)
    print(result)