def calculate_difference(value1, value2):
    try:
        num1 = float(value1)
        num2 = float(value2)
        return num1 - num2
    except (ValueError, TypeError):
        return None

if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 3.2
    result = calculate_difference(sample_a, sample_b)
    print(result)