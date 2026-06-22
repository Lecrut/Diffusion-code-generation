def generate_fibonacci_terms(count):
    if count <= 0:
        return []
    if count == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, count):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

if __name__ == '__main__':
    terms = generate_fibonacci_terms(100)
    print(terms)