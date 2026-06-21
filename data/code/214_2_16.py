def find_min_value(numbers):
    min_value = float('inf')
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 0.57, -1.23, 4.56]
    print(find_min_value(sample_values))