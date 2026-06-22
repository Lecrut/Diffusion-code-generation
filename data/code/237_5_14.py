def generate_sequence(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    sequence = [i**2 + i for i in range(1, n+1)]
    return sequence

if __name__ == '__main__':
    try:
        sample_sequence = generate_sequence(10)
        print(sample_sequence)
    except ValueError as e:
        print(e)