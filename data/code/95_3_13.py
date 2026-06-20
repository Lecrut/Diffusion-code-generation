def check_number(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError("Number must be a non-negative integer")
    return num > 0 and num % 2 == 0 and num < 100

if __name__ == '__main__':
    sample_values = [50, -10, 100, 3.14]
    for value in sample_values:
        try:
            print(f"{value}: {check_number(value)}")
        except ValueError as e:
            print(e)