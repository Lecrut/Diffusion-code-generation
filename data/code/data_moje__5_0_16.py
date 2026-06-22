def calculate_length_difference(length1, length2):
    try:
        val1 = float(length1)
        val2 = float(length2)
        diff = val1 - val2
        return diff
    except (TypeError, ValueError):
        return None

if __name__ == '__main__':
    sample_length_a = 10.5
    sample_length_b = 7.2
    result = calculate_length_difference(sample_length_a, sample_length_b)
    print(result)
    sample_length_c = "invalid"
    sample_length_d = 5
    result_error = calculate_length_difference(sample_length_c, sample_length_d)
    print(result_error)