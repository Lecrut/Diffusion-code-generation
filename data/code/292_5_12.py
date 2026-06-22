def trapezoid_perimeter(base1, base2, leg1, leg2):
    return base1 + base2 + leg1 + leg2

if __name__ == '__main__':
    perimeter = trapezoid_perimeter(5, 7, 3, 4)
    print(perimeter)