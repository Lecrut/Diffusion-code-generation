INITIAL_VALUE = 1
SEQUENCE_LENGTH = 10

def generate_sequence():
    sequence = [INITIAL_VALUE] * SEQUENCE_LENGTH
    for i in range(2, SEQUENCE_LENGTH):
        sequence[i] = sum(sequence[i-2:i]) + 1
    return sequence

if __name__ == '__main__':
    result = generate_sequence()
    for term in result:
        print(term)