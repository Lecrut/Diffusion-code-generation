def find_max_mixed(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_val = numbers[0]
    for item in numbers[1:]:
        if isinstance(item, (int, float)) and isinstance(max_val, (int, float)):
            if item > max_val:
                max_val = item
        else:
            raise TypeError("All elements must be numeric types")
    return max_val

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, -1]
    print(find_max_mixed(sample_values))