def calculate_difference(length1, length2):
    try:
        num1 = float(length1)
        num2 = float(length2)
        return abs(num1 - num2)
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be numeric values representing lengths.")

if __name__ == '__main__':
    sample_input_1 = "10.5"
    sample_input_2 = "3.2"
    try:
        result = calculate_difference(sample_input_1, sample_input_2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")