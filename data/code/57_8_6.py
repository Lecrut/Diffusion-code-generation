def generate_fibonacci(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs

if __name__ == '__main__':
    result = generate_fibonacci(1000)
    print(result[-1])