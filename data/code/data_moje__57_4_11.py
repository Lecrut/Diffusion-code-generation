def generate_fibonacci(n):
    if n <= 0:
        return []
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]

if __name__ == '__main__':
    result = generate_fibonacci(200)
    print(result)