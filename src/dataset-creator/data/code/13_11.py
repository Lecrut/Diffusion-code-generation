def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest
if __name__ == '__main__':
    sample_data = [3, 7, 2, 9, 4, 85, -10, 1]
    result = find_largest(sample_data)
    print(result)