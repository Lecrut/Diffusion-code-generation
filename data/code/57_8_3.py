def fibonacci_up_to_index(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    fibs = [0] * (n + 1)
    if n >= 1:
        fibs[1] = 1
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs

if __name__ == '__main__':
    result = fibonacci_up_to_index(1000)
    print(result)