def validate_integers(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both inputs must be integers.")

def is_greater_than(num1, num2):
    validate_integers(num1, num2)
    return num1 > num2

if __name__ == '__main__':
    sample_num1 = 25
    sample_num2 = 10
    try:
        result = is_greater_than(sample_num1, sample_num2)
        print(result)
    except ValueError as e:
        print(e)