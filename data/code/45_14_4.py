def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")
    min_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
    return min_value

if __name__ == '__main__':
    sample_data = [15, 3, 42, 7, 19, 1]
    result = find_minimum(sample_data)
    print(result)