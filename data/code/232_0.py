if __name__ == '__main__':
    a = 0
    b = 1
    count = 20
    sequence = []
    while len(sequence) < count:
        sequence.append(a)
        next_val = a + b
        a = b
        b = next_val
    print(*sequence)