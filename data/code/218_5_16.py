def find_minimum(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_values = [15, 3, 8, 22, 1]
    min_value = find_minimum(sample_values)
    print(min_value)