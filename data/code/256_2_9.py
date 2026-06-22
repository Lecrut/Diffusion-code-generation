def calculate_range(numbers):
    if not numbers:
        return None
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_data = [1.5, 3.2, 4.8, 6.1, 2.9]
    print(f"Range of {sample_data}: {calculate_range(sample_data)}")