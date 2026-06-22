def factorial_of_10_do_while_style():
    result = 1
    i = 1
    while True:
        result *= i
        i += 1
        if i > 10:
            break
    return result

if __name__ == '__main__':
    print(factorial_of_10_do_while_style())