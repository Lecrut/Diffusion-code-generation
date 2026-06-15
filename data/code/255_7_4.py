def find_max_float(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    sample_list = [3.14159, 2.71828, 1.61803, 4.0, 0.5]
    try:
        maximum = find_max_float(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)