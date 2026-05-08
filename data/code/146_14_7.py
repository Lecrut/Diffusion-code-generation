def process_numbers(numbers):
    all_conditions_met = False
    try:
        if not numbers:
            raise ValueError("Input list is empty")
        if all(isinstance(n, int) for n in numbers):
            flag1 = True
        else:
            flag1 = False
        if len(numbers) > 0 and all(n > 0 for n in numbers):
            flag2 = True
        else:
            flag2 = False
        if flag1 and flag2:
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
        print("All conditions successfully met.")
    else:
        print("One or more conditions failed to meet.")
if __name__ == '__main__':
    sample_data_success = [1, 2, 3, 4]
    sample_data_failure_type = [1, 2, "a", 4]
    sample_data_failure_value = [-1, 2, 3]
    sample_data_empty = []
    print("--- Test Case 1 (Success) ---")
    process_numbers(sample_data_success)
    print("\n--- Test Case 2 (Failure - Type Error) ---")
    process_numbers(sample_data_failure_type)
    print("\n--- Test Case 3 (Failure - Value Error) ---")
    process_numbers(sample_data_failure_value)
    print("\n--- Test Case 4 (Failure - Empty List) ---")
    process_numbers(sample_data_empty)