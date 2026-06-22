def find_min(numbers):
    if not numbers:
        return None

    current_min = numbers[0]

    for num in numbers:
        if num < current_min:
            current_min = num

    return current_min

if __name__ == '__main__':
    sample_numbers = [34, -11, 78, -5, 23, 0, 99]
    result = find_min(sample_numbers)
    print(result)