def growing_sequence(start, end):
    seq = []
    for i in range(start, end + 1):
        seq.append(i)
    return seq

if __name__ == '__main__':
    print(growing_sequence(1, 5))