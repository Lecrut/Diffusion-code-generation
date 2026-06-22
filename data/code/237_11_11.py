INITIAL_TERM = 5
COMMON_DIFFERENCE = 3
NUMBER_OF_TERMS = 15

def generate_arithmetic_progression(start=INITIAL_TERM, difference=COMMON_DIFFERENCE, terms=NUMBER_OF_TERMS):
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    progression = generate_arithmetic_progression()
    print(progression)