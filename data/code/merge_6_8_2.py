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
    num1_str_err = "ten"
    num2_str_ok = "5"
    result2 = calculate_product(num1_str_err, num2_str_ok)
    print(f"Product of {num1_str_err} and {num2_str_ok}: {result2}")
    num1_str_err2 = "hello"
    num2_str_err2 = "world"
    result3 = calculate_product(num1_str_err2, num2_str_err2)
    print(f"Product of {num1_str_err2} and {num2_str_err2}: {result3}")