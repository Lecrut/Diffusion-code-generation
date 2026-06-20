def calculate_length_difference(length1, length2):
    try:
        num1 = float(length1)
        num2 = float(length2)
        return abs(num1 - num2)
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be numeric values representing lengths.")

if __name__ == '__main__':
    sample_length1 = 150.5
    sample_length2 = 120.3
    result = calculate_length_difference(sample_length1, sample_length2)
    print(result)