def print_growing_sequence():
    term = 2
    for _ in range(6):
        print(term)
        term = round(term * 1.5)

if __name__ == '__main__':
    print_growing_sequence()