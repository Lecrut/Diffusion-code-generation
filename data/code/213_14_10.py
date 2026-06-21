def fibonacci(n):
    fibs = [0] * n
    for i in range(2, n):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs

if __name__ == '__main__':
    sample_n = 10
    output = fibonacci(sample_n)
    print(output)