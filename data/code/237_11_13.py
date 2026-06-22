def generate_arithmetic_progression(start=5, difference=3, terms=15):
    if not all(isinstance(i, (int, float)) and i >= 0 for i in [start, difference, terms]):
        raise ValueError("All inputs must be non-negative numbers.")
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    progression = generate_arithmetic_progression()
    print(progression)