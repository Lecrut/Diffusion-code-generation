def generate_growing_number_sequence(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    return ','.join(str(i) for i in range(1, n + 1))

if __name__ == '__main__':
    N = 5
    try:
        result = generate_growing_number_sequence(N)
        print(result)
    except ValueError as e:
        print(e)