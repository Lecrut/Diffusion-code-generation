def find_min_element(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for number in numbers:
        if number < min_val:
            min_val = number
    return min_val
if __name__ == '__main__':
    sample_values = [12, 45, 23, 78, 1, -9, 34, 0]
    result = find_min_element(sample_values)
    print(result)