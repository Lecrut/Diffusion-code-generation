def find_minimum(numbers):
    if not numbers:
        return None
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_values = [4, 2, 9, 7, 5, 1, 8, 3, 6]
    print(find_minimum(sample_values))