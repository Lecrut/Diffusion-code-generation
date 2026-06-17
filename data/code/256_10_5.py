def calculate_range(numbers):
    if not numbers:
        return 0
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum
if __name__ == '__main__':
    sample_list_one = [10, 5, 20, 15]
    sample_list_two = [42]
    sample_list_three = []
    sample_list_four = [1, 1, 1, 1]
    result_one = calculate_range(sample_list_one)
    result_two = calculate_range(sample_list_two)
    result_three = calculate_range(sample_list_three)
    result_four = calculate_range(sample_list_four)
    print(f"Range for {sample_list_one}: {result_one}")
    print(f"Range for {sample_list_two}: {result_two}")
    print(f"Range for {sample_list_three}: {result_three}")
    print(f"Range for {sample_list_four}: {result_four}")