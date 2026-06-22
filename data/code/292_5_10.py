def trapezoid_perimeter(base1, base2, leg1, leg2):
    return base1 + base2 + leg1 + leg2

if __name__ == '__main__':
    B1 = 5
    B2 = 7
    L1 = 3
    L2 = 4
    perimeter = trapezoid_perimeter(B1, B2, L1, L2)
    print(perimeter)