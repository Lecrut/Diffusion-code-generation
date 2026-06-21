def find_min_value(numbers):
    min_val = float('inf')
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 0.57, -1.23, 4.56]
    print(find_min_value(sample_values))