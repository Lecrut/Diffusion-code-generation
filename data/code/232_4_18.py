def generate_growing_numbers(N):
    for i in range(1, N + 1):
        yield i

if __name__ == '__main__':
    sample_value = 50
    result = list(generate_growing_numbers(sample_value))
    print(result)