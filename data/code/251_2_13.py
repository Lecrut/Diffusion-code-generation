def validate_input(input_list):
    if not all(isinstance(x, (int, float)) for x in input_list):
        raise ValueError("Error: Input contains non-numeric values.")

def determine_the_largest_number_present_batch_process(numbers):
    validate_input(numbers)
    return max(numbers)

if __name__ == '__main__':
    sample_values = [10, 5, 22, 8, 30]
    result = determine_the_largest_number_present_batch_process(sample_values)
    print(result)