def generate_fibonacci(n: int) -> list:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    sequence = [0] * n
    sequence[0] = 0
    sequence[1] = 1
    for i in range(2, n):
        sequence[i] = sequence[i-1] + sequence[i-2]
    return sequence

if __name__ == '__main__':
    result = generate_fibonacci(75)
    print(result)