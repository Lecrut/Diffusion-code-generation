def is_greater_than(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both inputs must be integers.")
    return num1 > num2

if __name__ == '__main__':
    try:
        sample_num1 = 25
        sample_num2 = 10
        result = is_greater_than(sample_num1, sample_num2)
        print(result)
    except ValueError as e:
        print(e)