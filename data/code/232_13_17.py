def print_growing_sequence():
    multiplier = 1.5
    term = 2
    for _ in range(6):
        print(round(term))
        term *= multiplier

if __name__ == '__main__':
    print_growing_sequence()