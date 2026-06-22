def factorial_do_while_style(n):
    result = 1
    counter = n
    while True:
        result *= counter
        counter -= 1
        if counter < 1:
            break
    return result

if __name__ == '__main__':
    print(factorial_do_while_style(10))