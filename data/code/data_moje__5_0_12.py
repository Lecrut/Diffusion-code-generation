def calculate_difference(length1, length2):
    try:
        val1 = float(length1)
        val2 = float(length2)
        return val1 - val2
    except ValueError:
        raise ValueError("Both inputs must be numeric values.")

if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 3.2
    result = calculate_difference(sample_a, sample_b)
    print(result)