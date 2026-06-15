def calculate_product(a, b):
    try:
        result = int(a) * int(b)
        return result
    except ValueError:
        return "Error: One or both inputs were not valid integers."
if __name__ == '__main__':
    num1_str = "10"
    num2_str = "5"
    print(calculate_product(num1_str, num2_str))
    num1_str_invalid = "ten"
    num2_str_valid = "5"
    print(calculate_product(num1_str_invalid, num2_str_valid))
    num1_str_invalid2 = "hello"
    num2_str_invalid2 = "world"
    print(calculate_product(num1_str_invalid2, num2_str_invalid2))