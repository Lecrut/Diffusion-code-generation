def generate_sequence(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    
    return (3 * i - 2 for i in range(1, n + 1))

if __name__ == '__main__':
    sequence = list(generate_sequence(10))
    print(sequence)