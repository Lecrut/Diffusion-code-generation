def find_min_max(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2, 9, 4]
    result = find_min_max(sample_values)
    print(f"Minimum: {result[0]}, Maximum: {result[1]}")