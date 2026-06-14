if __name__ == '__main__':
    a = 0
    b = 1
    sequence = []
    for _ in range(10):
        sequence.append(a)
        next_term = a + b
        a = b
        b = next_term
    for term in sequence:
        print(term)