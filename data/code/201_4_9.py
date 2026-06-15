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
    except ValueError:
        return "Error: Invalid input. Please ensure all parts are valid numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_input = "10,20,30,40,error,50"
    result = calculate_average(sample_input)
    print(result)
    sample_input_valid = "1,2,3,4,5"
    result_valid = calculate_average(sample_input_valid)
    print(result_valid)
    sample_input_empty = ""
    result_empty = calculate_average(sample_input_empty)
    print(result_empty)
    sample_input_only_text = "a,b,c"
    result_text = calculate_average(sample_input_only_text)
    print(result_text)