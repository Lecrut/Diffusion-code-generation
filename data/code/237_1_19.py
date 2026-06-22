START = 3
DIFFERENCE = 4
NUM_TERMS = 15

def generate_arithmetic_progression(start=START, difference=DIFFERENCE, terms=NUM_TERMS):
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    progression = generate_arithmetic_progression()
    print(progression)