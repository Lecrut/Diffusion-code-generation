def generate_arithmetic_progression(start, difference, terms):
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    sequence = generate_arithmetic_progression(3, 4, 15)
    print(sequence)