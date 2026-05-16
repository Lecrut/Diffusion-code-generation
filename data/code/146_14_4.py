def process_numbers(numbers):
    success = True
    try:
        if not numbers:
            success = False
        else:
            for num in numbers:
                if num < 0:
                    success = False
                    break
                if num % 2 != 0:
                    success = False
                    break
        if success:
            print("All numbers processed successfully.")
        else:
            print("Error: One or more conditions failed during processing.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    process_numbers(sample_data)
    sample_data_fail = [10, 25, 30, 40]
    process_numbers(sample_data_fail)
    sample_data_empty = []
    process_numbers(sample_data_empty)
    sample_data_negative = [10, -20, 30]
    process_numbers(sample_data_negative)