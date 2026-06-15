def find_maximum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.99]
    max_value = find_maximum(sample_list)
    print(max_value)