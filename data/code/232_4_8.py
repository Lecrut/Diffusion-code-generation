def generate_growing_numbers(N):
    numbers = []
    for i in range(1, N + 1):
        numbers.append(i)
    return numbers

if __name__ == '__main__':
    sample_value = 30
    result = generate_growing_numbers(sample_value)
    print(result)