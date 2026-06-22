def factorial_do_while_style(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    counter = 1
    while True:
        result *= counter
        counter += 1
        if counter > n:
            break
    return result

if __name__ == '__main__':
    number = 10
    computed_factorial = factorial_do_while_style(number)
    print(computed_factorial)