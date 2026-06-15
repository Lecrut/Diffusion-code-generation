def calculate_range(numbers):
    if not numbers:
        return 0
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum
if __name__ == '__main__':
    sample_list_one = [10, 5, 20, 15]
    result_one = calculate_range(sample_list_one)
    print(f"The range of {sample_list_one} is: {result_one}")
    sample_list_two = [3, 9, 1, 7]
    result_two = calculate_range(sample_list_two)
    print(f"The range of {sample_list_two} is: {result_two}")
    sample_list_empty = []
    result_empty = calculate_range(sample_list_empty)
    print(f"The range of {sample_list_empty} is: {result_empty}")
    sample_list_single = [42]
    result_single = calculate_range(sample_list_single)
    print(f"The range of {sample_list_single} is: {result_single}")