def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == '__main__':
    result = generate_fibonacci(20)
    print(result)