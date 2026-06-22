def construct_number_sequence(n):
    sequence = []
    for i in range(1, n + 1):
        sequence.append(str(i))
    return ','.join(sequence)

if __name__ == '__main__':
    N = 8
    result = construct_number_sequence(N)
    print(result)