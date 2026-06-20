def calculate_length_difference(length1, length2):
    try:
        value1 = float(length1)
        value2 = float(length2)
        return abs(value1 - value2)
    except (ValueError, TypeError):
        return None

if __name__ == '__main__':
    sample_length_1 = "10.5"
    sample_length_2 = "4.2"
    result = calculate_length_difference(sample_length_1, sample_length_2)
    print(result)