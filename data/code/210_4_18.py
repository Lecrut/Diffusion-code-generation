def calculate_range(values):
    if not values:
        return None
    lowest = min(values)
    highest = max(values)
    return (lowest, highest)

if __name__ == '__main__':
    sample_values1 = [4, 2, 9, 6, 5]
    sample_values2 = []
    sample_values3 = [-3, -1, -7, -2]
    sample_values4 = [100, 200, 300]

    print(f"Range of {sample_values1}: {calculate_range(sample_values1)}")
    print(f"Range of {sample_values2}: {calculate_range(sample_values2)}")
    print(f"Range of {sample_values3}: {calculate_range(sample_values3)}")
    print(f"Range of {sample_values4}: {calculate_range(sample_values4)}")