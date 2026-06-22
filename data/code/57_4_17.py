def generate_fibonacci(n):
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

if __name__ == '__main__':
    result = generate_fibonacci(200)
    print(result)