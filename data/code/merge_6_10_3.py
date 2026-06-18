if __name__ == '__main__':
    num1 = 12
    num2 = 5
    try:
        n1 = float(num1)
        n2 = float(num2)
        product = n1 * n2
        print(product)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")