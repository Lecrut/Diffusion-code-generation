if __name__ == '__main__':
    num1 = 100
    num2 = 7

    try:
        quotient = num1 // num2
        remainder = num1 % num2
        print(quotient)
        print(remainder)
    except Exception as e:
        print(f"Error: {e}")