SEQUENCE_START = 10
SEQUENCE_STEP = 5
SEQUENCE_LENGTH = 5

def generate_integers():
    for i in range(SEQUENCE_LENGTH):
        yield SEQUENCE_START + (i * SEQUENCE_STEP)

if __name__ == '__main__':
    gen = generate_integers()
    first_value = next(gen)
    print(first_value)