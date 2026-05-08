def process_numbers(numbers):
    all_conditions_met = False
    try:
        if not numbers:
            raise ValueError("Input list is empty")
        sum_of_numbers = sum(numbers)
        is_all_positive = all(n > 0 for n in numbers)
        has_even_sum = sum_of_numbers % 2 == 0
        if is_all_positive and has_even_sum:
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
    sample_data_success = [2, 4, 6, 8]
    sample_data_failure_positivity = [1, 2, -3, 4]
    sample_data_failure_sum = [1, 2, 4, 5]
    sample_data_empty = []
    print("--- Test Case 1 (Success) ---")
    process_numbers(sample_data_success)
    print("\n--- Test Case 2 (Failure: Positivity) ---")
    process_numbers(sample_data_failure_positivity)
    print("\n--- Test Case 3 (Failure: Sum) ---")
    process_numbers(sample_data_failure_sum)
    print("\n--- Test Case 4 (Failure: Empty) ---")
    process_numbers(sample_data_empty)