def compute_fibonacci_terms(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        last = sequence[-1]
        second_last = sequence[-2]
        new_val = last + second_last
        sequence.append(new_val)
    return sequence

if __name__ == '__main__':
    result = compute_fibonacci_terms(100)
    for term in result:
        print(term)