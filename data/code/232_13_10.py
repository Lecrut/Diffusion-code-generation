def print_growing_sequence():
    term = 2
    multiplier = 1.5
    for _ in range(6):
        print(round(term))
        term *= multiplier

if __name__ == '__main__':
    print_growing_sequence()