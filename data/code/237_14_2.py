def generate_sequence(num_terms):
    return [2**i for i in range(num_terms)]

if __name__ == '__main__':
    print(generate_sequence(5))