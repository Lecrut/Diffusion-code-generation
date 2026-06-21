def find_min_value(numbers):
    min_val = float('inf')
    for number in numbers:
        if number < min_val:
            min_val = number
    return min_val

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618, 0.577, -1.414]
    print(find_min_value(sample_values))