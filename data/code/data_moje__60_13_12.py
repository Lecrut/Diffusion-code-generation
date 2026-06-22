def compute_factorial(n):
    result = 1
    i = 1
    while True:
        if i > n:
            break
        result *= i
        i += 1
    return result

if __name__ == '__main__':
    print(compute_factorial(10))