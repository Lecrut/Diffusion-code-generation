def generate_sequence(n):
    sequence = [1, 1]
    for i in range(2, n):
        next_term = sum(sequence[-2:]) + 1
        sequence.append(next_term)
    return sequence

if __name__ == '__main__':
    terms_count = 10
    result = generate_sequence(terms_count)
    for term in result:
        print(term)