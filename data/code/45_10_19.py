def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    current_min = numbers[0]
    for number in numbers:
        if number < current_min:
            current_min = number
    return current_min

if __name__ == '__main__':
    sample_data = [34, 12, 5, 89, 1, 45, 67, 2]
    result = find_minimum(sample_data)
    print(result)