def generate_fibonacci(n: int) -> list:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

if __name__ == '__main__':
    result = generate_fibonacci(500)
    print(result)