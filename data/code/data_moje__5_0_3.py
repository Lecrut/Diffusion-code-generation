def calculate_length_difference(length1, length2):
    try:
        val1 = float(length1)
        val2 = float(length2)
        return abs(val1 - val2)
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be numeric values.")

if __name__ == '__main__':
    sample_length1 = "10.5"
    sample_length2 = "3.2"
    result = calculate_length_difference(sample_length1, sample_length2)
    print(result)