def is_strictly_greater(num1, num2):
    return num1 > num2

def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")

if __name__ == '__main__':
    try:
        sample_num1 = 10
        sample_num2 = 5
        validate_integer(sample_num1)
        validate_integer(sample_num2)
        result = is_strictly_greater(sample_num1, sample_num2)
        print(result)
    except ValueError as e:
        print(e)