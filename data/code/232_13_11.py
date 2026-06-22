def print_growing_sequence(start=2, terms=6):
    term = start
    for _ in range(terms):
        print(round(term))
        term *= 1.5

if __name__ == '__main__':
    try:
        print_growing_sequence()
    except Exception as e:
        print(f"An error occurred: {e}")