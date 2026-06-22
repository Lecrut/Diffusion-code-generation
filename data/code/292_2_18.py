def herons_formula(a, b, c):
    if not all(isinstance(side, (int, float)) and side > 0 for side in [a, b, c]):
        raise ValueError("All sides must be positive numbers.")
    
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

if __name__ == '__main__':
    print(herons_formula(3, 4, 5))