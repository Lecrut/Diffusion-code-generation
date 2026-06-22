if __name__ == '__main__':
    a, b = 0, 1
    sequence = []
    for _ in range(20):
        sequence.append(a)
        a, b = b, a + b
    print(sequence)