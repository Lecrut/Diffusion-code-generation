def find_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, -2, 7]
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum: {min_val}, Maximum: {max_val}")