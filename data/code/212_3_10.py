def find_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

if __name__ == '__main__':
    input_data = [15, 3, 88, 42, 9, 71]
    minimum_val, maximum_val = find_min_max(input_data)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")