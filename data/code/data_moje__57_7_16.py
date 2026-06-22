def compute_fibonacci_terms(count: int) -> list[int]:
    if count <= 0:
        return []
    if count == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < count:
        current = sequence[-1]
        previous = sequence[-2]
        next_val = (current << 1) - previous
        sequence.append(next_val)
    return sequence

if __name__ == '__main__':
    n_terms = 100
    result = compute_fibonacci_terms(n_terms)
    for i, val in enumerate(result):
        print(f"{i}: {val}")