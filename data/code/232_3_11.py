def generate_growing_sequence(n):
    return ','.join(str(i) for i in range(1, n + 1))

if __name__ == '__main__':
    N = 5
    result = generate_growing_sequence(N)
    print(result)