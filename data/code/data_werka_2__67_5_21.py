def add_numbers(a, b):
    try:
        result = float(a) + float(b)
        return result
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be numbers")

if __name__ == '__main__':
    sample_a = 5
    sample_b = '10'
    print(add_numbers(sample_a, sample_b))