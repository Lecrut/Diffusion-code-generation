def check_number(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")
    if n <= 0:
        return "Number is not positive"
    if n % 2 != 0:
        return "Number is not even"
    if n >= 100:
        return "Number is not less than 100"
    return "Number is positive, even, and less than 100"

if __name__ == '__main__':
    sample_values = [50, -10, 101, 51, 0]
    for val in sample_values:
        result = check_number(val)
        print(f"Input: {val}, Result: {result}")