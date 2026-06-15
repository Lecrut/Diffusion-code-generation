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
    sample_input_2 = "1,2,3,4"
    result_2 = calculate_average(sample_input_2)
    print(result_2)
    sample_input_3 = "a,b,c"
    result_3 = calculate_average(sample_input_3)
    print(result_3)
    sample_input_4 = ""
    result_4 = calculate_average(sample_input_4)
    print(result_4)