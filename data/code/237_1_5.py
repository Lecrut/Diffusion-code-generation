def arithmetic_progression(start, difference, terms):
    if not all(isinstance(i, (int, float)) for i in [start, difference, terms]):
        raise ValueError("All input values must be numbers.")
    if terms < 0:
        raise ValueError("Number of terms must be non-negative.")
    
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    sequence = arithmetic_progression(3, 4, 15)
    print(sequence)