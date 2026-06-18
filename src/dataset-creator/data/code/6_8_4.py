def calculate_product(a, b):
    try:
        result = int(a) * int(b)
        return result
    except ValueError:
        return "Error: One or both inputs are not valid integers."
if __name__ == '__main__':
    num1_str = "10"
    num2_str = "5"
    result1 = calculate_product(num1_str, num2_str)
    print(f"Product of {num1_str} and {num2_str}: {result1}")
    num3_str = "hello"
    num4_str = "3"
    result2 = calculate_product(num3_str, num4_str)
    print(f"Product of {num3_str} and {num4_str}: {result2}")
    num5_str = "-2"
    num6_str = "7"
    result3 = calculate_product(num5_str, num6_str)
    print(f"Product of {num5_str} and {num6_str}: {result3}")