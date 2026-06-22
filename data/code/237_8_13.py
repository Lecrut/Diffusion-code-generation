INITIAL_VALUE = 1

def generate_sequence(n):
    sequence = [INITIAL_VALUE] * n
    for i in range(2, n):
        sequence[i] = sum(sequence[:i-1]) + 1
    return sequence

if __name__ == '__main__':
    result = generate_sequence(10)
    print(result)