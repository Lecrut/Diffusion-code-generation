if __name__ == '__main__':
    num1 = 5
    num2 = 10
    product = 1
    counter = 0
    while counter < 2:
        if counter == 0:
            product = num1
        elif counter == 1:
            product = num1 * num2
        counter += 1
    print(product)