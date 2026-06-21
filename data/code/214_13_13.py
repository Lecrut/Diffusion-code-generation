def find_min_value(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values_1 = [7, 3, 9, 2, 5]
    sample_values_2 = [-3, -1, -4, -2, -5]
    sample_values_3 = [10]
    sample_values_4 = []

    print(f"Minimum in {sample_values_1}: {find_min_value(sample_values_1)}")
    print(f"Minimum in {sample_values_2}: {find_min_value(sample_values_2)}")
    print(f"Minimum in {sample_values_3}: {find_min_value(sample_values_3)}")
    print(f"Minimum in {sample_values_4}: {find_min_value(sample_values_4)}")