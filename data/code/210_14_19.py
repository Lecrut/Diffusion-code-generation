def calculate_range(data):
    if not data:
        return 0
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum

if __name__ == '__main__':
    sample_data_1 = [10, 5, 20, 3, 15]
    range_1 = calculate_range(sample_data_1)
    print(f"Data: {sample_data_1}")
    print(f"Range: {range_1}")

    sample_data_2 = [5.5, 1.2, 8.9, 3.0]
    range_2 = calculate_range(sample_data_2)
    print(f"\nData: {sample_data_2}")
    print(f"Range: {range_2}")

    sample_data_3 = []
    range_3 = calculate_range(sample_data_3)
    print(f"\nData: {sample_data_3}")
    print(f"Range: {range_3}")