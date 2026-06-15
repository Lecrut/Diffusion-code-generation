def calculate_product(a, b):
    try:
        result = int(a) * int(b)
        return result
    except ValueError:
        return "Error: Both inputs must be integers."
if __name__ == '__main__':
    num1_str = "10"
    num2_str = "5"
    result1 = calculate_product(num1_str, num2_str)
    print(f"Product of {num1_str} and {num2_str}: {result1}")
    num1_str_error = "ten"
    num2_str_error = "5"
    result2 = calculate_product(num1_str_error, num2_str_error)
    print(f"Product of {num1_str_error} and {num2_str_error}: {result2}")
    num1_str_error2 = "10"
    num2_str_error2 = "three"
    result3 = calculate_product(num1_str_error2, num2_str_error2)
    print(f"Product of {num1_str_error2} and {num2_str_error2}: {result3}")