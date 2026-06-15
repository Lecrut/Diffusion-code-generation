if __name__ == '__main__':
    num1 = 5
    num2 = 10
    product = 1
    count = 0
    while count < 2:
        if count == 0:
            product = num1
        elif count == 1:
            product = num1 * num2
        count += 1
    print(product)