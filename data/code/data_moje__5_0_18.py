def calculate_difference(length1, length2):
    try:
        val1 = float(length1)
        val2 = float(length2)
        return abs(val1 - val2)
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be valid numeric values.")

if __name__ == '__main__':
    sample_length_a = 10.5
    sample_length_b = 4.2
    result = calculate_difference(sample_length_a, sample_length_b)
    print(result)