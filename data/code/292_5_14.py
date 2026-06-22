TRAPEZOID_PERIMETER_CONSTANT = 1

def calculate_perimeter(base1, base2, leg1, leg2):
    return (base1 + base2 + leg1 + leg2) * TRAPEZOID_PERIMETER_CONSTANT

if __name__ == '__main__':
    base1_value = 5
    base2_value = 7
    leg1_value = 3
    leg2_value = 4
    perimeter = calculate_perimeter(base1_value, base2_value, leg1_value, leg2_value)
    print(perimeter)