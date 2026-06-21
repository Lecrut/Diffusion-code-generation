def get_median_value(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    sorted_numbers = sorted(numbers)
    mid_index = len(sorted_numbers) // 2
    return sorted_numbers[mid_index]

if __name__ == "__main__":
    sample_data = [7, 1, 3, 9, 5]
    print(get_median_value(sample_data))