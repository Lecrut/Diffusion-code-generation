INITIAL_TERM = 1
SEQUENCE_LENGTH = 10

def generate_sequence():
    sequence = [INITIAL_TERM, INITIAL_TERM]
    for _ in range(2, SEQUENCE_LENGTH):
        next_term = sum(sequence[-2:]) + 1
        sequence.append(next_term)
    return sequence

if __name__ == '__main__':
    result = generate_sequence()
    for term in result:
        print(term)