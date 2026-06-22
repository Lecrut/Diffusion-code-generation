def get_fibonacci_sequence(n: int) -> list:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == '__main__':
    result = get_fibonacci_sequence(200)
    print(result)