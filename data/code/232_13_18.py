def print_growing_sequence(start=2, multiplier=1.5, terms=6):
    term = start
    for _ in range(terms):
        print(round(term))
        term *= multiplier

if __name__ == '__main__':
    print_growing_sequence()