if __name__ == '__main__':
    num1 = 15
    num2 = 7
    try:
        product = num1 * num2
        print(product)
    except TypeError:
        print("Error: Invalid input types.")