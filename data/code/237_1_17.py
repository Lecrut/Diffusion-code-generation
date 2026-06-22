def generate_arithmetic_progression(start, difference, terms):
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    start = 3
    difference = 4
    terms = 15
    sequence = generate_arithmetic_progression(start, difference, terms)
    print(sequence)