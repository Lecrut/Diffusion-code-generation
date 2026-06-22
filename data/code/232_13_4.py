def print_growing_sequence():
    terms = [2]
    for _ in range(5):
        terms.append(round(terms[-1] * 1.5))
    for term in terms:
        print(term)

if __name__ == '__main__':
    print_growing_sequence()