def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both a and b must be numbers")

def sum_ab(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    sample_a = 42
    sample_b = 7
    print(sum_ab(sample_a, sample_b))