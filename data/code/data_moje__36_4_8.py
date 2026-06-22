TRAPEZOID_DIVISOR = 2

def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / TRAPEZOID_DIVISOR

if __name__ == '__main__':
    val_b1 = 6.0
    val_b2 = 10.0
    val_h = 5.0
    result = trapezoid_area(val_b1, val_b2, val_h)
    print(result)