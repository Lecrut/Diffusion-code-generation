def first_n_fibonacci(n=200):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    print(first_n_fibonacci(200))