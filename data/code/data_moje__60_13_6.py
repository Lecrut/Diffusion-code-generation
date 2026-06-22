def factorial(n):
    result = 1
    i = 1
    while True:
        result *= i
        i += 1
        if i > n:
            break
    return result

if __name__ == '__main__':
    number = 10
    print(factorial(number))