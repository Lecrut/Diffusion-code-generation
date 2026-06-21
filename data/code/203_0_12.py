def compare_numbers(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        if num_a > num_b:
            return 'Greater'
        elif num_b > num_a:
            return 'Lesser'
        else:
            return 'Equal'
    except ValueError:
        raise ValueError("Both inputs must be valid floating-point numbers.")

if __name__ == '__main__':
    sample_num1 = "3.14159"
    sample_num2 = "2.71828"
    try:
        result = compare_numbers(sample_num1, sample_num2)
        print(result)
    except ValueError as e:
        print(e)