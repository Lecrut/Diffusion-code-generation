def generate_sequence(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    sequence = [1, 1]
    for i in range(2, n):
        next_term = sum(sequence[-2:]) + 1
        sequence.append(next_term)
    return sequence

if __name__ == '__main__':
    result = generate_sequence(10)
    for term in result:
        print(term)