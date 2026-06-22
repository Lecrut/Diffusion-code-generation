def generate_growing_numbers(N):
    return list(range(1, N + 1))

if __name__ == '__main__':
    sample_value = 50
    result = generate_growing_numbers(sample_value)
    print(result)