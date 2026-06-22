def compute_factorial_do_while(n):
    result = 1
    i = 2
    while True:
        result *= i
        i += 1
        if i > n:
            break
    return result

if __name__ == '__main__':
    print(compute_factorial_do_while(10))