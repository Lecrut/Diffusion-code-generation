def check_number(num):
    if not isinstance(num, int) or num <= 0 or num >= 100:
        raise ValueError("Input must be a positive integer less than 100")
    return num % 2 == 0

if __name__ == '__main__':
    sample_values = [42, -10, 100, 3.14]
    for value in sample_values:
        try:
            print(f"{value}: {check_number(value)}")
        except ValueError as e:
            print(e)