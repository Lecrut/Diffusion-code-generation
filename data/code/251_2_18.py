def validate_input(input_list):
    if not input_list:
        return False
    for item in input_list:
        if not isinstance(item, (int, float)):
            return False
    return True

def determine_the_largest_number_present_batch_process(numbers):
    if not validate_input(numbers):
        raise ValueError("Invalid input. Please ensure all inputs are valid numbers.")
    return max(numbers)

if __name__ == '__main__':
    sample_values = [10, 5, 22, 8, 30]
    try:
        result = determine_the_largest_number_present_batch_process(sample_values)
        print(result)
    except ValueError as e:
        print(e)