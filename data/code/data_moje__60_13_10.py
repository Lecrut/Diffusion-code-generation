def factorial():
    result = 1
    n = 10
    i = 2
    while True:
        result *= i
        i += 1
        if i > n:
            break
    return result

if __name__ == '__main__':
    print(factorial())