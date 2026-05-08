def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    test_list_1 = [1, 2, 3, 4, 5]
    test_list_2 = [10, 20, 30]
    test_list_3 = []
    test_list_4 = [-1, 0, 1]
    try:
        avg1 = calculate_average(test_list_1)
        print(f"Average of {test_list_1}: {avg1}")
        avg2 = calculate_average(test_list_2)
        print(f"Average of {test_list_2}: {avg2}")
        avg4 = calculate_average(test_list_4)
        print(f"Average of {test_list_4}: {avg4}")
        try:
            calculate_average(test_list_3)
        except ValueError as e:
            print(f"Caught expected error for empty list: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")