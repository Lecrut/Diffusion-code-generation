def arithmetic_progression(start, difference, terms):
    if not all(isinstance(i, (int, float)) and i >= 0 for i in [start, difference]):
        raise ValueError("Start and difference must be non-negative numbers")
    if not isinstance(terms, int) or terms <= 0:
        raise ValueError("Number of terms must be a positive integer")
    
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    print(arithmetic_progression(3, 4, 15))