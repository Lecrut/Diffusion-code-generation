def generate_sequence(count):
    return [i for i in range(1, count + 1)]

if __name__ == '__main__':
    sample_count = 50
    sequence = generate_sequence(sample_count)
    print(*sequence, sep='\n')