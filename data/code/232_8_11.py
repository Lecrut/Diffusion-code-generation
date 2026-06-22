def growing_sequence(start, end):
    sequence = [None] * (end - start + 1)
    for i in range(start, end + 1):
        sequence[i - start] = i
    return sequence

if __name__ == '__main__':
    print(growing_sequence(1, 5))