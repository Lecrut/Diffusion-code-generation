def fibonacci_sequence(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    sequence = [0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == '__main__':
    result = fibonacci_sequence(1000)
    print(result)