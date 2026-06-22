def validate_inputs(start, difference, terms):
    if not all(isinstance(x, (int, float)) for x in [start, difference]):
        raise ValueError("Start and difference must be numbers")
    if not isinstance(terms, int) or terms <= 0:
        raise ValueError("Terms must be a positive integer")

def generate_arithmetic_progression(start=5, difference=3, terms=15):
    validate_inputs(start, difference, terms)
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    progression = generate_arithmetic_progression()
    print(progression)