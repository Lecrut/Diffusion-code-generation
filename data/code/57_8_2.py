def generate_fibonacci_up_to_index(n):
    if n < 0:
        raise ValueError("Index must be non-negative")
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    sequence = [0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

if __name__ == '__main__':
    sample_index = 1000
    result = generate_fibonacci_up_to_index(sample_index)
    print(f"Sequence length: {len(result)}")
    print(f"Value at index 0: {result[0]}")
    print(f"Value at index 1: {result[1]}")
    print(f"Value at index 500: {result[500]}")
    print(f"Value at index 1000: {result[1000]}")