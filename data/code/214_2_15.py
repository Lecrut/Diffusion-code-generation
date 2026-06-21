def find_min_value(numbers):
    min_value = float('inf')
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 7.8, -2.4, 0.0]
    print(find_min_value(sample_values))