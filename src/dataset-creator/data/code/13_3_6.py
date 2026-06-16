def find_maximum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    sample_values = [3, 7, 2, 9, 4, -5, 8]
    result = find_maximum(sample_values)
    print(result)