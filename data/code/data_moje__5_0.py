def calculate_difference(value1, value2):
    try:
        num1 = float(value1)
        num2 = float(value2)
        return num1 - num2
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be numeric values.")

if __name__ == '__main__':
    sample_input_1 = "15.5"
    sample_input_2 = "7.2"
    result = calculate_difference(sample_input_1, sample_input_2)
    print(result)