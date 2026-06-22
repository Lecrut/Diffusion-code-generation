def generate_growing_number_sequence(n):
    if n <= 0:
        raise ValueError("n must be greater than 0")
    
    sequence = [str(i) for i in range(1, n + 1)]
    return ','.join(sequence)

if __name__ == '__main__':
    N = 5
    result = generate_growing_number_sequence(N)
    print(result)