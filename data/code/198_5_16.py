def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_values = [4, 1, 3, 2, 5]
    try:
        result = find_minimum(sample_values)
        print("Minimum value:", result)
    except ValueError as e:
        print(e)