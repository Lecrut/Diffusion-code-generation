def check_equality(num1_str, num2_str):
    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
        return num1 == num2
    except ValueError:
        return False
if __name__ == '__main__':
    num1_str = "10"
    num2_str = "10"
    result = check_equality(num1_str, num2_str)
    print(result)