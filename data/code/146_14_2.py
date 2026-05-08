def process_numbers(numbers):
    all_conditions_met = False
    try:
        if not numbers:
            raise ValueError("Input list is empty")
        sum_of_numbers = sum(numbers)
        all_even = all(n % 2 == 0 for n in numbers)
        has_positive = any(n > 0 for n in numbers)
        if sum_of_numbers > 0 and all_even and has_positive:
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
    process_numbers(sample_data)
    print("-" * 20)
    sample_data_fail = [1, 2, 3, 4]
    process_numbers(sample_data_fail)
    print("-" * 20)
    sample_data_empty = []
    process_numbers(sample_data_empty)