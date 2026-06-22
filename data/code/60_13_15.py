def factorial_do_while(n):
    result = 1
    multiplier = 1
    while True:
        result *= multiplier
        multiplier += 1
        if multiplier > n:
            break
    return result

if __name__ == '__main__':
    print(factorial_do_while(10))