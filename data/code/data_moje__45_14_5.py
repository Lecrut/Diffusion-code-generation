def find_minimum(numbers):
    if not numbers:
        return None
    current_min = numbers[0]
    for number in numbers[1:]:
        if number < current_min:
            current_min = number
    return current_min

if __name__ == '__main__':
    sample_values = [34, 15, 88, 2, 57, 90, 12]
    result = find_minimum(sample_values)
    print(result)