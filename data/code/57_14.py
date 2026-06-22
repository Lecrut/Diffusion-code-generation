def generate_fibonacci(n):
    fibs = [0, 1]
    for _ in range(n - 2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

if __name__ == '__main__':
    print(generate_fibonacci(15))