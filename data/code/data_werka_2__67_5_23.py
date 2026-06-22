def add_numbers(a, b):
    try:
        result = float(a) + float(b)
        return result
    except ValueError:
        raise ValueError("Both inputs must be numbers")

if __name__ == '__main__':
    sample_value1 = "3.5"
    sample_value2 = "4.7"
    print(add_numbers(sample_value1, sample_value2))