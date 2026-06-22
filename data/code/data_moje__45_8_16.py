def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list of integers cannot be empty.")
    minimum_value = numbers[0]
    for number in numbers[1:]:
        if number < minimum_value:
            minimum_value = number
    return minimum_value

if __name__ == '__main__':
    sample_data = [34, 12, 5, 89, 1, 42]
    result = find_minimum(sample_data)
    print(result)