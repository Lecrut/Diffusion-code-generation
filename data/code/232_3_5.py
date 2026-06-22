def generate_growing_number_sequence(n):
    SEPARATOR = ','
    sequence = ','.join(str(i) for i in range(1, n + 1))
    return sequence

if __name__ == '__main__':
    N = 5
    result = generate_growing_number_sequence(N)
    print(result)