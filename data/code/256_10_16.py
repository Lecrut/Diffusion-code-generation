def calculate_range(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 15]
    try:
        range1 = calculate_range(sample_list1)
        print(f"Range of {sample_list1}: {range1}")
    except ValueError as e:
        print(e)

    sample_list4 = [100, 1, 50]
    try:
        range4 = calculate_range(sample_list4)
        print(f"Range of {sample_list4}: {range4}")
    except ValueError as e:
        print(e)