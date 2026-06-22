def growing_sequence(limit):
    return (x for x in range(1, limit + 1))

if __name__ == '__main__':
    limit = 10
    sequence = growing_sequence(limit)
    print(list(sequence))