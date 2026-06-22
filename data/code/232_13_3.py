def print_growing_sequence():
    term = 2
    for _ in range(6):
        print(round(term))
        term *= 1.5

if __name__ == '__main__':
    print_growing_sequence()