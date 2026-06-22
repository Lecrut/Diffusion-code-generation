def get_first_n_fibonacci(n: int) -> list:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == '__main__':
    count = 200
    result = get_first_n_fibonacci(count)
    print(result)