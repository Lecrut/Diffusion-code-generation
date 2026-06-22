def generate_fibonacci(n):
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]

if __name__ == '__main__':
    count = 200
    result = generate_fibonacci(count)
    print(result)