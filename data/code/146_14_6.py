def process_numbers(numbers):
    all_conditions_met = True
    try:
        if not numbers:
            all_conditions_met = False
        else:
            for num in numbers:
                if not isinstance(num, int):
                    all_conditions_met = False
                    break
                if num <= 0:
                    all_conditions_met = False
                    break
        if all_conditions_met:
            print("All numbers are positive integers.")
        else:
            print("One or more conditions failed.")
    except Exception as e:
        print(f"An error occurred during processing: {e}")
if __name__ == '__main__':
    sample_numbers_success = [1, 5, 10, 15]
    sample_numbers_failure_type = [1, 5, "ten", 15]
    sample_numbers_failure_value = [1, 5, -10, 15]
    sample_numbers_failure_empty = []
    print("--- Test Case 1 (Success) ---")
    process_numbers(sample_numbers_success)
    print("\n--- Test Case 2 (Failure - Type Error) ---")
    process_numbers(sample_numbers_failure_type)
    print("\n--- Test Case 3 (Failure - Value Error) ---")
    process_numbers(sample_numbers_failure_value)
    print("\n--- Test Case 4 (Failure - Empty List) ---")
    process_numbers(sample_numbers_failure_empty)