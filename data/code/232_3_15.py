def create_growing_sequence(limit):
    sequence = []
    for number in range(1, limit + 1):
        sequence.append(str(number))
    return ','.join(sequence)

if __name__ == '__main__':
    LIMIT = 7
    result = create_growing_sequence(LIMIT)
    print(result)