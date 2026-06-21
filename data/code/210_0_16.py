def find_min_max(numbers):
    if not numbers:
        return None, None
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

if __name__ == '__main__':
    sample_values = [10, 5, 22, 8, 30, 1]
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum: {min_val}, Maximum: {max_val}")