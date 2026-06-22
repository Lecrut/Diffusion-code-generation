def generate_growing_number_sequence(n):
    return ','.join(str(i) for i in range(1, n + 1))

if __name__ == '__main__':
    print(generate_growing_number_sequence(5))