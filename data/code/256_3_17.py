def calculate_range(numbers):
    if not numbers:
        raise ValueError("Input set cannot be empty")
    min_value = min(numbers)
    max_value = max(numbers)
    return max_value - min_value

if __name__ == '__main__':
    sample_set1 = {5, 3, 9, 1, 7}
    sample_set2 = {10, 4, 8, 6, 2}
    sample_set3 = set()
    sample_set4 = {15}

    print(f"Range of {sample_set1}: {calculate_range(sample_set1)}")
    print(f"Range of {sample_set2}: {calculate_range(sample_set2)}")
    try:
        print(f"Range of {sample_set3}: {calculate_range(sample_set3)}")
    except ValueError as e:
        print(f"Error for {sample_set3}: {e}")
    print(f"Range of {sample_set4}: {calculate_range(sample_set4)}")