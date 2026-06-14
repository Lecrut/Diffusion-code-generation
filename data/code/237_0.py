if __name__ == '__main__':
    n = 20
    a = 0
    b = 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        next_val = a + b
        a = b
        b = next_val
    print(sequence)