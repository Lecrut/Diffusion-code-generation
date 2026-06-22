def generate_sequence(start_value, length):
    return list(map(lambda n: start_value + (n - 1) * 5, range(1, length + 1)))

if __name__ == '__main__':
    sample_sequence = generate_sequence(100, 15)
    print(sample_sequence)