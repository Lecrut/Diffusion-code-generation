def generate_sequence(n):
    return (3 * i - 2 for i in range(1, n + 1))

if __name__ == '__main__':
    sequence = generate_sequence(10)
    for term in sequence:
        print(term)