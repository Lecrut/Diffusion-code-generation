def process_numbers(numbers):
    all_conditions_met = False
    try:
        if not numbers:
            raise ValueError("Input list is empty")
        sum_of_numbers = sum(numbers)
        is_positive = all(n > 0 for n in numbers)
        has_zero = 0 in numbers
        is_even_sum = sum_of_numbers % 2 == 0
        if is_positive and not has_zero and is_even_sum:
            all_conditions_met = True
        else:
            all_conditions_met = False
    except ValueError as e:
        print(f"Error during processing: {e}")
        all_conditions_met = False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        all_conditions_met = False
    if all_conditions_met:
        print("All conditions successfully met. Processing complete.")
    else:
        print("One or more conditions failed. Message not printed.")
if __name__ == '__main__':
    sample_data = [2, 4, 6, 8]
    print("--- Test Case 1 ---")
    process_numbers(sample_data)
    sample_data_fail = [1, 2, -3, 4]
    print("\n--- Test Case 2 ---")
    process_numbers(sample_data_fail)
    sample_data_zero = [1, 2, 3, 0]
    print("\n--- Test Case 3 ---")
    process_numbers(sample_data_zero)
    sample_data_empty = []
    print("\n--- Test Case 4 ---")
    process_numbers(sample_data_empty)