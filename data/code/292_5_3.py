def trapezoid_perimeter(base1, base2, leg1, leg2):
    return base1 + base2 + leg1 + leg2

if __name__ == '__main__':
    bases_and_legs = {
        'base1': 5,
        'base2': 7,
        'leg1': 3,
        'leg2': 4
    }
    
    perimeter = trapezoid_perimeter(**bases_and_legs)
    print(perimeter)