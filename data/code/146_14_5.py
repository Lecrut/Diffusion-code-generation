def process_numbers(numbers):
    all_conditions_met = False
    try:
        if not numbers:
            raise ValueError("Input list is empty")
        sum_of_numbers = sum(numbers)
        all_positive = all(n > 0 for n in numbers)
        has_even = any(n % 2 == 0 for n in numbers)
        if sum_of_numbers > 0 and all_positive and has_even:
            all_conditions_met = True
        else:
            all_conditions_met = False
    except ValueError as e:
        print(f"Error during processing: {e}")
        all_conditions_met = False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        all_conditions_met = False
    return all_conditions_met
if __name__ == '__main__':
    sample_data = [2, 4, 6, 8]
    result = process_numbers(sample_data)
    if result:
        print("All conditions successfully met. The sequence is valid.")
    else:
        print("One or more conditions failed to meet the requirements.")
    sample_data_fail = [1, 3, 5]
    result_fail = process_numbers(sample_data_fail)
    if result_fail:
        print("All conditions successfully met. The sequence is valid.")
    else:
        print("One or more conditions failed to meet the requirements.")