def find_minimum(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_data2 = [7, 34, 5, 28, 9, 6, 1]
    min_value = find_minimum(sample_data2)
    print(f"Minimum of {sample_data2}: {min_value}")