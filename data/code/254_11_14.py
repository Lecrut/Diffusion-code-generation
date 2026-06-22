def find_min(numbers):
    if not numbers:
        return None
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, -2.1, 0.0, 7.6]
    print(find_min(sample_values))