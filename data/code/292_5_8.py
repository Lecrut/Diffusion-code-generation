def trapezoid_perimeter(base1, base2, leg1, leg2):
    if not all(isinstance(i, (int, float)) and i > 0 for i in [base1, base2, leg1, leg2]):
        raise ValueError("All inputs must be positive numbers.")
    return base1 + base2 + leg1 + leg2

if __name__ == '__main__':
    perimeter = trapezoid_perimeter(5, 7, 3, 4)
    print(perimeter)