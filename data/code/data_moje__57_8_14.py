def fibonacci_up_to_index(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    sequence = [0] * (n + 1)
    if n >= 1:
        sequence[1] = 1
    for i in range(2, n + 1):
        sequence[i] = sequence[i - 1] + sequence[i - 2]
    return sequence

if __name__ == '__main__':
    result = fibonacci_up_to_index(1000)
    print(result)