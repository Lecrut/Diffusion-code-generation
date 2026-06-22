def compute_fib_sequence(limit: int) -> list:
    if limit <= 0:
        return []
    if limit == 1:
        return [0]
    sequence = [0, 1]
    [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, limit)]
    return sequence

if __name__ == '__main__':
    target_count = 15
    result_sequence = compute_fib_sequence(target_count)
    print(result_sequence)