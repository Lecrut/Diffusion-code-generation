def calculate_average(data_string):
    numbers = []
    try:
        parts = data_string.split(',')
        for part in parts:
            if part.strip():
                numbers.append(float(part.strip()))
            else:
                raise ValueError("Empty segment found")
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
    except ValueError as e:
        print(f"Error processing input: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
if __name__ == '__main__':
    sample_input_valid = "10,20,30,40,50"
    sample_input_invalid = "10,20,thirty,40"
    sample_input_empty = ""
    sample_input_only_commas = ",,"
    result1 = calculate_average(sample_input_valid)
    print(f"Average for '{sample_input_valid}': {result1}")
    result2 = calculate_average(sample_input_invalid)
    print(f"Average for '{sample_input_invalid}': {result2}")
    result3 = calculate_average(sample_input_empty)
    print(f"Average for '{sample_input_empty}': {result3}")
    result4 = calculate_average(sample_input_only_commas)
    print(f"Average for '{sample_input_only_commas}': {result4}")