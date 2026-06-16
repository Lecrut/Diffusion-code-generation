def find_maximum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum
if __name__ == '__main__':
    sample_list = [3, 75, 42, 98, 6, -10, 23]
    result = find_maximum(sample_list)
    print(result)