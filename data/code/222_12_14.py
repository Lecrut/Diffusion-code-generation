def find_min_value(numbers):
    min_val = float('inf')
    for number in numbers:
        if number < min_val:
            min_val = number
    return min_val

if __name__ == '__main__':
    sample_data = [3.14, 2.718, 1.618, 0.577, 0.314]
    result = find_min_value(sample_data)
    print(result)