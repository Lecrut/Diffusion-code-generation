def find_min_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 9.99]
    result = find_min_value(sample_list)
    print(result)