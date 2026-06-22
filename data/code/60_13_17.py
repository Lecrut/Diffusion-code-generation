def factorial(n):
    result = 1
    while True:
        result *= n
        n -= 1
        if n < 1:
            break
    return result

if __name__ == '__main__':
    print(factorial(10))