def generate_growing_numbers(N):
    if not isinstance(N, int) or N <= 0:
        raise ValueError("N must be a positive integer")
    
    return list(range(1, N + 1))

if __name__ == '__main__':
    sample_value = 50
    result = generate_growing_numbers(sample_value)
    print(result)