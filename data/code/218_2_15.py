def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_list = [3.14, 2.718, 1.618, -0.5, 9.99]
    minimum_value = find_minimum(sample_list)
    print(minimum_value)