def calculate_length_difference(length1, length2):
    try:
        num1 = float(length1)
        num2 = float(length2)
        return abs(num1 - num2)
    except (ValueError, TypeError):
        return None

if __name__ == '__main__':
    sample_length1 = 10.5
    sample_length2 = 3.2
    result = calculate_length_difference(sample_length1, sample_length2)
    print(result)

    sample_invalid1 = "abc"
    sample_invalid2 = 5.0
    result_invalid = calculate_length_difference(sample_invalid1, sample_invalid2)
    print(result_invalid)

    sample_negative1 = -2.5
    sample_negative2 = 4.5
    result_negative = calculate_length_difference(sample_negative1, sample_negative2)
    print(result_negative)