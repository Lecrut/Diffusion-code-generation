def factorial_do_while_style(n):
    result = 1
    i = 1
    while True:
        result *= i
        i += 1
        if i > n:
            break
    return result

if __name__ == '__main__':
    print(factorial_do_while_style(10))