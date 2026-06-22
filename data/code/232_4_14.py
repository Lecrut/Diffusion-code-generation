def generate_growing_numbers(N):
    if N < 1:
        raise ValueError("N must be greater than or equal to 1")
    return range(1, N + 1)

if __name__ == '__main__':
    sample_value = 50
    result = generate_growing_numbers(sample_value)
    print(list(result))