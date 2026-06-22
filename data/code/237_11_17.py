def validate_input(start, difference, terms):
    if not isinstance(start, (int, float)):
        raise ValueError("Start must be an integer or float")
    if not isinstance(difference, (int, float)):
        raise ValueError("Difference must be an integer or float")
    if not isinstance(terms, int) or terms <= 0:
        raise ValueError("Terms must be a positive integer")

def generate_arithmetic_progression(start=5, difference=3, terms=15):
    validate_input(start, difference, terms)
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    progression = generate_arithmetic_progression()
    print(progression)