def find_min_max(numbers):
    return min(numbers), max(numbers) if numbers else (None, None)

if __name__ == '__main__':
    input_data = [15, 3, 88, -5, 42, 9]
    minimum_val, maximum_val = find_min_max(input_data)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")