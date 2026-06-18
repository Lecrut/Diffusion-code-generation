def find_maximum(numbers):
    if not numbers:
        raise ValueError("List must contain at least one number.")
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum
if __name__ == '__main__':
    sample_numbers = [3, 7, 2, 9, 4, 8]
    result = find_maximum(sample_numbers)
    print(result)