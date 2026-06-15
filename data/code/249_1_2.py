def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    sample_list = [10, 5, 22, 8, 30, 15]
    result = find_largest(sample_list)
    print(result)