def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")
    min_value = numbers[0]
    for value in numbers[1:]:
        if value < min_value:
            min_value = value
    return min_value

if __name__ == '__main__':
    sample_list = [15, 4, 28, 2, 99, 33]
    result = find_minimum(sample_list)
    print(result)