def find_min_max(numbers):
    if not numbers:
        return None, None
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return minimum, maximum

if __name__ == '__main__':
    sample_data1 = [34, 78, 12, 90, 56]
    min_val, max_val = find_min_max(sample_data1)
    print(f"Data set 1: {sample_data1}")
    print(f"Minimum: {min_val}, Maximum: {max_val}")