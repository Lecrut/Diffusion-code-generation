def calculate_sum(input_string):
    try:
        numbers = input_string.split()
        total_sum = 0
        for item in numbers:
            total_sum += int(item)
        return total_sum
    except ValueError:
        return "Error: Input contains non-integer values."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_input = "10 25 30 45"
    result = calculate_sum(sample_input)
    print(result)
    sample_input_with_error = "10 25 hello 45"
    result_error = calculate_sum(sample_input_with_error)
    print(result_error)
    sample_input_empty = ""
    result_empty = calculate_sum(sample_input_empty)
    print(result_empty)